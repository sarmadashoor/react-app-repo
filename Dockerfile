# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Build the React app
RUN npm run build

# Serve the built app using a simple Node server
RUN npm install -g serve
CMD ["serve", "-s", "build"]

# Expose the port the app runs on
EXPOSE 3000
