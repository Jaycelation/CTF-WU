FROM node:22-alpine

WORKDIR /app

COPY package.json package-lock.json index.html report.html server.js bot.js ./
RUN apk update && apk upgrade
RUN apk add chromium
RUN npm install --only=production

EXPOSE 3000

CMD ["node", "server.js"]
