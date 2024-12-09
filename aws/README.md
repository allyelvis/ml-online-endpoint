### AWS SageMaker Online Endpoint
Steps to create and deploy an online endpoint using SageMaker.
1. Run `create_model.py` to create the model.
2. Run `create_endpoint.py` to create and deploy the endpoint.
3. Test the endpoint using SageMaker runtime API:
   ```python
   runtime = boto3.client('sagemaker-runtime')
   response = runtime.invoke_endpoint(
       EndpointName='my-endpoint',
       Body=b'{"key": "value"}',
       ContentType='application/json'
   )
   print(response['Body'].read())
