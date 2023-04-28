FROM node:latest

WORKDIR /code

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000
ENV PORT 3000

