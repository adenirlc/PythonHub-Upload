import os

import github

g = github.Github("", "")  # Username and Password of your account, or Access Token

print("-=" * 30)
print(f"Username: {g.get_user().login}\nFull Name: {g.get_user().name}\nEmail: {g.get_user().email}")
print("-=" * 30)

print("Write the name of repository to create:")
repo = input("> ")
private = False
print("Will the repository be Private or Public?\n1 - Private\n2 - Public")
setPP = int(input("> "))
if setPP == 1:
    private = True
r = g.get_user().create_repo(repo, private=private, description="This repository is created using a PythonHub-Upload.")

print("Write the path of folder to upload:")
path = input("> ")


def getFileContent(file):
    with open(file, 'r') as afile:
        return afile.read()


if os.path.exists(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for fname in files:
                root2 = root.replace(path, "")
                root2 = root2.replace("\\", "/")
                if root2 != "" or root2 == "/":
                    root2 = f"{root2}/"
                if root2.startswith("/"):
                    root2 = root2[1:]
                if not root2.startswith(".idea") or not root2.startswith(".git"):
                    print(f"File *{root2}{fname}* created with success.")
                    r.create_file(f"{root2}{fname}", "File Creation", f'{getFileContent(f"{root}/{fname}")}')
        print(f"The repository url is https://github.com/{g.get_user().login}/{r.name}")
    else:
        print("Write a path of folder, and no file.")
else:
    print("The path not exists.")
