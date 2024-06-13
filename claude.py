import boto3
import json

prompt_data="""
Human: You are an expert social media content generator. Draft an exciting and socially-
engaging blog post for a major travel website and newsletter. The post should be a travel guide
for Iceland that highlights recommended attractions, restaurants, and sights to see, along
with tips and tricks for travel.
Each paragraph should focus on a different topic, such as travel tips & tricks, best sights to
see, best food to eat, and so on. Within each topic, whenever there is a list (such as a list of
foods or a list of places), make each item on the list its own line with its own short
description. Name each thematic paragraph with just the name of the paragraph (NEVER a marker
like "paragraph 1" etc.). Include a call to action to buy tickets now at the end of the post.
The audience for this text is people excited to travel but who have never been to Iceland
before. The goal of the article is to drum up excitement for Iceland and leave readers with the
impression that the travel website is a trusted source of information for travel to Iceland.
Write your response in markdown format.
NEVER generate text before the article. Generate the article only (including the title).
Assistant:
"""
#bedrock client
bedrock=boto3.client(service_name="bedrock-runtime")

payload={
    "prompt":prompt_data,
    "max_tokens_to_sample":512,
    "temperature":0.5,
    "top_p":0.9,
}
body=json.dumps(payload)
model_id="anthropic.claude-v2"
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
repsonse_text=response_body['completion']
print(repsonse_text)