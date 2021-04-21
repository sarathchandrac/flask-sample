# Install python 3
FROM python:3
# Set /usr/src/app as the Working Directory
WORKDIR /usr/src/app
# copy the requirements file to the the current working directory
COPY requirements.txt .
# Install the required dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy all the files from current directory to tWORKDIR path of the virtual directory 
COPY . .
# EXPOSE 5000 
# ENTRYPOINT [ "python" ] 
CMD [ "python",  "app.py" ] 
