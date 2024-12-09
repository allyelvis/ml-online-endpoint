#### **`aws/create_model.py`**
```python
import boto3

sagemaker = boto3.client('sagemaker')
response = sagemaker.create_model(
    ModelName='my-ml-model',
    PrimaryContainer={
        'Image': 'your-container-image',
        'ModelDataUrl': 's3://your-model-data-path',
    },
    ExecutionRoleArn='your-sagemaker-role'
)
print(response)
