# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3 AS backend-stage

ARG DB_PASSWORD
ARG DB_USER
ARG DB_HOST
ARG DB_NAME

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

ENV POSTGRES_PASSWORD $DB_PASSWORD
ENV POSTGRES_DB $DB_NAME
ENV POSTGRES_USER $DB_USER
ENV POSTGRES_HOST $DB_HOST
ENV BACKEND_PORT 8080

# create root directory for our project in the container
RUN mkdir /backend

# Set the working directory to /backend
WORKDIR /backend

# Copy the current directory contents into the container at /backend
COPY ./backend/MyProject/* /backend/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE $BACKEND_PORT

# build stage Frontend
FROM node:13-alpine as build-stage

ENV VUE_APP_API_ENDPOINT "http://localhost:${BACKEND_PORT}/"
ENV ENTRY_PORT 80
ENV NODE_ENV production

WORKDIR /app 
COPY ./frontend ./
RUN \ 
	npm install \
	npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY ./frontend/nginx.config /etc/nginx/conf.d/default.conf
COPY --from=backend-stage /backend /backend
COPY --from=build-stage /app /app
#COPY --from=build-stage /app/dist /usr/share/nginx/html
# COPY --from=build-stage /app/dist /app

EXPOSE $ENTRY_PORT

CMD ["python", "manage.py", "runserver", "0.0.0.0:${$BACKEND_PORT}"]
CMD ["nginx", "-g", "daemon off;"]

