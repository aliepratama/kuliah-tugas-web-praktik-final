from flask import request
from tools_api.helpers.db import supabase
from tools_api.helpers.res_message import SuccessMessage, ErrorMessage
import tools_api.helpers.response as res
import replicate

prompts = ["Simple", "Unique", "Effective", "Durable", "Representative"]

def consult(user_id):
    results = []
    img_url = request.form.get('img_url')
    if img_url:
        response = supabase.table('users').select('token').eq('id', user_id).execute()
        if len(response.data) > 0:
            token = response.data[0]['token']
            print('TOKEN>>>>>', token)
            if token > 0:
                try:
                    for prompt in prompts:
                        try:
                            output = replicate.run(
                                    "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
                                    input={
                                        "image": img_url,
                                        "task": "visual_question_answering",
                                        "caption": "logo",
                                        "question": f"is this {prompt} look logo?"
                                    }
                                )
                            results.append(str(output).lower().find('yes') > -1)
                        except:
                            return res.server_error()
                    supabase.table('users').update({'token': token - 1}).eq('id', user_id).execute()
                    return res.ok(results, SuccessMessage.SM5)
                except Exception as e:
                    print(e)
                    return res.server_error()
            return res.bad_request(ErrorMessage.EM10)
    return res.bad_request(ErrorMessage.EM11)
