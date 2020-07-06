import json

# import requests


def lambda_handler(event, context):

    event.Records.map(async (record) => {
      try {
        await smsResponder(record)
      } catch (err) {
        console.error(err)
        return err
      }
    })

    return {
        "statusCode": 200,
    }
