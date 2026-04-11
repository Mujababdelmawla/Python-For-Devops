import time 

# Ask for user confirmation to start the deployment :
confirm = input("Are you sure you want to start the deployment? (yes/no)").lower()
if confirm != 'yes':
    print("The Deployment Has Been Canceled...")
    exit(0)

# Ask for Environment to deploy:
env = input("which environment would you like to deploy to ? (production/testing)").lower()
if env == 'production':
    print("Deploying to production environment...")
    time.sleep(5)
    print("production deployment has been completed successfully.")

elif env == 'testing':
    print("Deploying to testing environment ...")
    time.sleep(5)
    print("testing deployment has been completed successfully.")

else:
    print("Invalid Environment...Deployment failed .....!!!!!!")