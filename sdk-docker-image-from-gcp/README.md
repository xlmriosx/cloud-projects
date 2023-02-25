#  🧰 Simple way to install SDK from GCP.

---

## 🔗Related content 
### You can find post related in:
👨‍💻[DEV](https://dev.to/xlmriosx/how-upload-data-in-format-json-to-datastore-from-gcp-20no) 

### You can find video related in:
📺[YouTube](https://youtu.be/2oHaQeKkmWI)

### You can connect with me in:
🧬[LinkedIn](https://www.linkedin.com/in/xlmriosx/) 

--- 

### Resume 🧾

I will install Docker image to use it as a SDK in Console GCP.

For more information and potential of this, click [here](https://cloud.google.com/sdk/docs/downloads-docker).

---

### 1st - Pull Docker image ⬇

To use the image of the latest Cloud SDK release we will need pull image from repository in console.

I use following command:

CONSOLE:
```
docker pull gcr.io/google.com/cloudsdktool/cloud-sdk:latest
```

OUTPUT:
```
latest: Pulling from google.com/cloudsdktool/cloud-sdk
50e431f79093: Pull complete
6005b060ba7d: Pull complete
c49059196e30: Pull complete
Digest: sha256:fd9985597827057effdb04fd1b07db9463f4a00ac24684cd3726c05e146eafa1
Status: Downloaded newer image for gcr.io/google.com/cloudsdktool/cloud-sdk:latest
gcr.io/google.com/cloudsdktool/cloud-sdk:latest
```

---

### 2nd - Verifying installation ✅

Verify the installation (if you've pulled the latest version) by running the following command:

CONSOLE:
```
docker run gcr.io/google.com/cloudsdktool/cloud-sdk:latest gcloud version
```

OUTPUT:
```
Google Cloud SDK 284.0.0
alpha 2020.03.06
app-engine-go
app-engine-java 1.9.78
app-engine-python 1.9.88
app-engine-python-extras 1.9.88
beta 2020.03.06
bigtable
bq 2.0.54
cbt
cloud-datastore-emulator 2.1.0
core 2020.03.06
datalab 20190610
gsutil 4.48
kubectl 2020.03.06
pubsub-emulator 0.1.0
```

---

### 3rd - Authenticate with the gcloud 👤

We need authenticate to use gcloud tools. We can do that by the following command:

CONSOLE:
```
docker run -ti --name gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk gcloud auth login
```

Note: Once we've authenticated successfully, credentials are preserved in the volume of the gcloud-config container.

OUTPUT:
```
Go to the following link in your browser:

    https://accounts.google.com/o/oauth2/auth?...


Enter verification code: ********

You are now logged in as [xlmriosx@gmail.com].
Your current project is [xlmriosx].  You can change this setting by running:
  $ gcloud config set project PROJECT_ID
```

---

### 4th - Creating an alias 🔤

For simplicty create an alias by running:

CONSOLE:
```
alias csdk='docker run --rm --volumes-from gcloud-config -v ~/:/home/shared gcr.io/google.com/cloudsdktool/cloud-sdk'
```

You can change if you want. In my case I prefer 'csdk' like a nice alias.

---

### 5th - List your projects 📄

We can list projects by two forms a large and a short.

Large:
CONSOLE:
```
docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk gcloud projects list
```

Short:
CONSOLE:
```
csdk gcloud projects list
```


OUTPUT:
```
PROJECT_ID              NAME              PROJECT_NUMBER
xlmriosx                xlmriosx          783709003945
```

---

### 6th - Prove change of a project 🔀

We can change name of projects by two ways a large and a short.

Large:
CONSOLE:
```
docker run --rm --volumes-from gcloud-config gcr.io/google.com/cloudsdktool/cloud-sdk gcloud config set project $PROJECT_NAME
```

Short:
CONSOLE:
```
csdk gcloud config set project $PROJECT_NAME
```


OUTPUT:
```
Updated property [core/project].
```

---

### 7th - Say thanks, give like and share if this has been of help/interest 😁🖖

---
