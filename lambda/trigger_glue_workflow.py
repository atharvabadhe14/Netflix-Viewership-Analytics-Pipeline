import boto3

def lambda_handler(event, context):
    glue = boto3.client("glue", region_name="us-east-1")

    glue.start_workflow_run(
        Name="netflix-etl-workflow"
    )

    return {
        "statusCode": 200,
        "body": "Glue workflow triggered successfully"
    }
