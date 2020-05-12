# SLS serverless framework examples
1. Install Serverless framework
2. Create new IAM user profile and get credentials
3. Configure Serverless framework
4. serverless config credentials --provider aws --key <key> --secret <secret> --profile <profile-name>
5. Deploy: sls deploy -v
   Deploy one lambda only: sls deploy function -f <function-name>. Call function from aws-cli: sls invoke -f <function-name>
   Logs for function: sls logs -f <function-name> -t (t as a tail - stream logs in realtime)
6. Cleanup the stack: sls remove