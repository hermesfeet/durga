from __future__ import print_function
from request_api_ai import query_api_ai
import random
import json
from skills import skills_table


def build_speechlet_response(title, speech_output, should_end_session, card_output=None, reprompt_text=None):
    if not card_output:
        card_output = speech_output
    if not reprompt_text:
        reprompt_text = "Can you please respond?"
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': speech_output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': card_output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def on_session_started(session_started_request, session):
    """ Called when the session starts """
    print(
        "on_session_started requestId=" + session_started_request['requestId'] + ", sessionId=" + session['sessionId'])


def on_launch(skill_d, launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    # Dispatch to your skill's launch
    speechlet = build_speechlet_response(
        title=skill_d['title'],
        speech_output=random.choice(skill_d['welcome']),
        should_end_session=False,
        card_output=None, reprompt_text=None)

    return build_response(dict(), speechlet=speechlet)


def get_help_intent(skill):
    speechlet = build_speechlet_response(
        title=skill['title'],
        speech_output=random.choice(skill['help']),
        should_end_session=False,
        card_output=None, reprompt_text=None)

    return build_response(dict, speechlet=speechlet), None, None


def handle_session_end_request(skill):
    card_title = skill['title']
    speech_output = random.choice(skill['end_session'])
    speechlet = build_speechlet_response(title=card_title, speech_output=speech_output, should_end_session=True)
    return build_response(session_attributes=dict(), speechlet=speechlet)


def on_intent(event, skill, intent_request, session):
    """
    Called when the user specifies an intent for this skill
    """

    intent_name = intent_request['intent']['name']
    print('session')
    print(session)
    # raw_input('pause')

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    print('intent_request: ' + str(intent_request))
    print('intent_name: ', intent_name)

    if intent_name in ["AMAZON.HelpIntent"]:
        return get_help_intent(skill)

    elif intent_name in ["AMAZON.CancelIntent", "AMAZON.StopIntent"]:
        return handle_session_end_request(skill), None, None

    else:
        try:
            speech_query = intent_request['intent']['slots']['parsed_text']['value']
        except KeyError:
            print("ERROR, couldn't get speech query!")

            return get_help_intent(skill)

        speechlet, api_ai_request, api_ai_response = \
            speech_query_to_speechlet_response_and_intent(event=event, skill=skill, session_id=session.get('sessionId'),
                                                          speech_query=speech_query)

        return \
            build_response(session_attributes=None, speechlet=speechlet), \
            api_ai_request, \
            api_ai_response, \
            intent_name


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


def speech_query_to_speechlet_response_and_intent(event, skill, session_id, speech_query):
    # try:
    if True:
        api_ai_request, api_ai_response = query_api_ai(
            event=event,
            speech_query=speech_query,
            authorization=skill['api_ai_authorization_bearer'],
            api_ai_agent=skill['api_ai_agent'],
            session_id=session_id
        )
        print("Just queried API AI")
        print("agents response: ", json.dumps(api_ai_response))
        should_end_session = False
        if api_ai_response.get('result') and api_ai_response.get('result').get('contexts'):
            for context in api_ai_response.get('result').get('contexts'):
                if context['name'] == 'end_conversation':
                    should_end_session = True

        if api_ai_response['result']['fulfillment'].get('messages'):
            return build_speechlet_response(
                title=skill['title'],
                speech_output=api_ai_response['result']['fulfillment']['messages'][0]['speech'],
                should_end_session=should_end_session
            ), api_ai_request, api_ai_response
        else:
            return build_speechlet_response(
                title=skill['title'],
                speech_output=api_ai_response['result']['fulfillment']['speech'],
                should_end_session=should_end_session
            ), api_ai_request, api_ai_response

            # except:
            #     print('EXCEPTION!!!! The API.AI webhook probaly failed')
            #     return build_speechlet_response(
            #         title=skill['title'],
            #         speech_output=random.choice(skill['apology']),
            #         should_end_session=True
            #     ), 'API.AI WEBHOOK PROBABLY FAILED'


def build_response(session_attributes, speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet
    }


def inner_lambda_handler(event, context):
    """
    Returns the speechlet object and intent
    :param event:
    :param context:
    :return: returns a tuple - the amazon_response, api_ai_request, api_ai_response, intent
    """

    print("event.session.application.applicationId=" + event['session']['application']['applicationId'])

    if event['session']['application']['applicationId'] not in skills_table.keys():
        raise ValueError("Invalid Application ID")

    skill = skills_table[event['session']['application']['applicationId']]
    print('Agent: ', skill['title'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(skill, event['request'], event['session']), None, None, "LaunchRequest"

    elif event['request']['type'] == "IntentRequest":
        return on_intent(
            event=event,
            skill=skill,
            intent_request=event['request'],
            session=event['session'])

    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session']), None, None, "SessionEndedRequest"

    raise Exception("I don't understand, I thought all request types were one of the three handled by lambda handler")


def lambda_handler(event, context):
    """
    Wraps inner_lambda_handler. Logs event. Calls chatbase.
    :param event: alexa_custom_skill/generic_connector/tests/generic_connector_2_req.json
    :param context:
    :return: See alexa_custom_skill/generic_connector/tests/generic_connector_2_res.json
    """
    print('event: ')
    print(json.dumps(event))
    print('type(context):')
    print(type(context))
    print('context')
    print(context)
    print('context as json: ')
    print(json.dumps(get_context_dict(context)))

    response, api_ai_request, api_ai_response, intent = inner_lambda_handler(event, context)

    log_to_process = dict()
    log_to_process['type'] = 'log_to_process'
    log_to_process['event'] = event

    log_to_process['response'] = response
    log_to_process['skill'] = skills_table[event['session']['application']['applicationId']]
    log_to_process['api_ai_request'] = api_ai_request
    log_to_process['api_ai_response'] = api_ai_response
    log_to_process['intent'] = intent

    print('type(log_to_process): ', type(log_to_process))
    print('log_to_process: ', log_to_process)
    print(json.dumps(log_to_process))
    return response


def get_context_dict(context):
    if context:
        return {
            "function_name": context.function_name,
            "function_version": context.function_version,
            "invoked_function_arn": context.invoked_function_arn,
            "memory_limit_in_mb": context.memory_limit_in_mb,
            "aws_request_id": context.aws_request_id,
            "log_group_name": context.log_group_name,
            "log_stream_name": context.log_stream_name,
            "client_context": context.client_context
        }
    else:
        return None
