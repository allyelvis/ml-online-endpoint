import boto3

sagemaker = boto3.client('sagemaker')
response = sagemaker.create_endpoint_config(
    EndpointConfigName='my-endpoint-config',
    ProductionVariants=[
        {
            'VariantName': 'AllTraffic',
            'ModelName': 'my-ml-model',
            'InitialInstanceCount': 1,
            'InstanceType': 'ml.m5.large',
        }
    ]
)
print(response)

response = sagemaker.create_endpoint(
    EndpointName='my-endpoint',
    EndpointConfigName='my-endpoint-config'
)
print(response)
