import subprocess


if __name__ == "__main__":
    print("\n--------------------\n" + \
          "Migrating models...\n")

    subprocess.run(["python", "stock_graphql_api/manage.py", "makemigrations"])
    subprocess.run(["python", "stock_graphql_api/manage.py", "migrate"])

    print("\nDone!")

    print("--------------------\n" + \
          "Starting app...")

    subprocess.Popen(["python", "stock_graphql_api/manage.py", "runserver"])

    print("--------------------\n" + \
      "Scheduling jobs...")

    subprocess.Popen(["python", "scheduled_task.py"])

    print("--------------------\n" + \
          "COMPLETED\n" + \
          "--------------------")