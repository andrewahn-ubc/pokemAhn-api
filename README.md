## Instructions on how to pull changes (for myself)
1. Set up an EC2 instance then connect to it using
<br> `ssh -i "replace/with/path/to/pem/file" ec2-user@REPLACE_WITH_PUBLIC_IP`
2. Move into repo
<br> `cd pokemAhn-api/` <br>
3. If you want to pull git pull now
<br> `git pull origin main` <br>
4. Attach to tmux session
<br> `tmux attach` <br>
5. Rerun the server
<br> "Ctrl + C" to stop the server<br>
`gunicorn -k uvicorn.workers.UvicornWorker server:app --bind 0.0.0.0:8000 --workers 1` <br>
6. Dettach from tmux session <br>
"Ctrl + B", then "D" <br>
7. Close SSH connection <br>
`exit`
