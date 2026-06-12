FROM node:20-alpine
COPY package.json /package.json
RUN npm install
COPY report.js /report.js
CMD ["node", "/report.js"]