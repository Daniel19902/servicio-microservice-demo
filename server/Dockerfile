# build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
COPY . .
CMD ["node", "index.js"]
