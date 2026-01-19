# DE-Zoomcamp-HW1

**Question 1:**

Step 1:
make container for image python=3.13

```bash
docker run -it --rm\
-v $(pwd)/app:app/test\
-- entrypoint=bash\
python:3.13
```
Step 2:
Check the version of PIP

```bash
pip --version
```
output
![alt text](image.png)

**Question 2:**

Step 1:
Make docker-compose.yaml in our directory 

Step 2:
run docker compose

```bash 
docker-compose up
```

step 3:
acsess pgAdmin in browser by browsing to http://localhost:8080

step 4:
Login with email: pgadmin@pgadmin.com, password: pgadmin

step 5:
Configure:
- General tab: 
Name: pgdatabase

- Connection tab:
Host: postgres (the container name)
Port: 5432
Username: postgres
Password: postgres

output
![alt text](image-1.png)
![alt text](image-2.png)