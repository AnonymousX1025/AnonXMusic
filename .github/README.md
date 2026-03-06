<div align="center">

<h2>AnonXMusic</h2>

<b>Telegram Group Calls Streaming Bot</b><br>
Supports YouTube, Spotify, Resso, Apple Music, SoundCloud and M3U8 links.

<a href="https://github.com/AnonymousX1025/AnonXMusic/stargazers">
    <img src="https://img.shields.io/github/stars/AnonymousX1025/AnonXMusic?color=blueviolet&logo=github&logoColor=black&style=for-the-badge" alt="Stars"/>
</a>
<a href="https://github.com/AnonymousX1025/AnonXMusic/network/members">
    <img src="https://img.shields.io/github/forks/AnonymousX1025/AnonXMusic?color=blueviolet&logo=github&logoColor=black&style=for-the-badge" alt="Forks"/>
</a>
<a href="https://github.com/AnonymousX1025/AnonXMusic/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License"/>
</a>
<a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Written%20in-Python-blue?style=for-the-badge&logo=python" alt="Python"/>
</a>
<br>

<img src="https://github.com/AnonymousX1025/AnonXMusic/blob/master/.github/anonx.jpg" width="720" height="auto">

AnonXMusic lets you stream high-quality and low-latency audio and video playback into telegram group video chats.<br>
Built with Python, Pyrogram, and Py-TgCalls, it’s optimized for reliability and easy deployment on Heroku, VPS, or Docker.
</div>

<hr>

<h2>🔥 Features</h2>

- 🎧 Stream low-latency audio in real time to <b>Telegram group video chats</b>
- 🌐 Supports multiple platforms like <b>YouTube, Spotify, Apple Music, SoundCloud</b>
- ⚡ Advanced queue management with auto-play
- ⚙️ Easy deployment — works on Local, VPS, or Heroku
- ❤️ Built with Python
<hr>

<h2>☁️ Manual Deployment</h2>

<h3>✔️ Prerequisites</h3>

- <a href="https://www.python.org">Python 3.10+</a> installed  
- <a href="https://deno.com/">Deno</a> & <a href="https://ffmpeg.org//">FFmpeg</a> installed on your system  

#### Installing Deno and FFmpeg

**On Ubuntu/Debian:**
```bash
# Update package list
sudo apt update

# Install FFmpeg
sudo apt install -y ffmpeg

# Install Deno
curl -fsSL https://deno.land/install.sh | sh
# Add Deno to PATH (restart shell or run: export PATH="$HOME/.deno/bin:$PATH")
```

**On macOS (using Homebrew):**
```bash
# Install FFmpeg
brew install ffmpeg

# Install Deno
brew install deno
```

**On Windows:**
- Download and install FFmpeg from <a href="https://ffmpeg.org/download.html">official site</a>
- Install Deno from <a href="https://deno.com/">deno.com</a>

- Required variables mentioned in <a href="https://github.com/AnonymousX1025/AnonXMusic/blob/master/sample.env">sample.env</a>

<details>
    <summary>
        <h3>Local / VPS Setup</h3>
    </summary>

```bash
git clone https://github.com/AnonymousX1025/AnonXMusic && cd AnonXMusic

# Install dependencies
pip3 install -U -r requirements.txt

# Rename and configure environment variables
mv sample.env .env
# Edit .env with your credentials

# Start the bot
bash start
```
</details>

<details>
    <summary>
        <h3>Deploy to Heroku</h3>
    </summary>

> Click on the button below to deploy on Heroku<br>
    <a href="https://dashboard.heroku.com/new?template=https://github.com/AnonymousX1025/AnonXMusic">
        <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-black?style=for-the-badge&logo=heroku"/>
    </a>
</details>

<hr>

<h2>⚙️ Configuration</h2>

Edit <code>.env</code> (or set variables in your hosting environment):
<details>
    <summary>Here's an example of the .env file</summary>

```env
API_ID=123456
API_HASH=abcdef1234567890
BOT_TOKEN=123456:ABC-DEF
OWNER_ID=123456789
LOGGER_ID=-1001234567890
MONGO_URL=mongodb+srv://
SESSION=BQgfh...AA
```

> 📝 Check <a href="https://github.com/AnonymousX1025/AnonXMusic/blob/master/config.py">config.py</a> for all available options.
</details>

<hr>

<h2>🧐 Usage</h2>

1. Add the bot to your Telegram group.  
2. Promote it to <b>admin</b> with invite users permission.  
3. Use commands in the chat to control playback:
<details>
    <summary>Commands overview</summary>
    <pre>
/play [song name or link] -> Play audio in the videochat
/vplay [song name or link] -> Play video in the videochat
/pause -> Pause playback
/resume -> Resume playback
/skip -> Skip to next track
/stop -> Stop playback
/seek -> Seeks the stream
/queue -> Show queue
    </pre>
</details>

<hr>

<h2>❤️ Contributing</h2>

Contributions are welcome!

1. Fork the repository.  
2. Create your branch: <code>git checkout -b feature/new</code>.  
4. Commit changes: <code>git commit -m 'New feature'</code>.  
5. Push: <code>git push origin feature/new</code>
6. Open a Pull Request.

<hr>

<h2>🗒️ License</h2>

This project is licensed under the <b>MIT License</b> — see <a href="https://github.com/AnonymousX1025/AnonXMusic/blob/master/LICENSE">LICENSE</a> for details.

<hr>

<h2>🤞 Updates and support</h2>

- <a href="https://FallenAssociation.t.me">Updates channel</a>
- <a href="https://DevilsHeavenMF.t.me">Support group</a>

<hr>

<h2>👀 Acknowledgements</h2>

- Inspired by other open-source Telegram music bots.
- Thanks to all the <a href="https://github.com/AnonymousX1025/AnonXMusic/graphs/contributors">contributors</a>.

<hr>

<h2>🔧 Troubleshooting</h2>

### RuntimeError: Deno and FFmpeg must be installed and accessible in the system PATH.
- Ensure Deno and FFmpeg are installed as per the Prerequisites section.
- On Linux, after installing Deno, restart your shell or run `export PATH="$HOME/.deno/bin:$PATH"` to add it to PATH.
- Verify installation: `which deno && which ffmpeg`

### Import errors or missing dependencies
- Install Python dependencies: `pip3 install -U -r requirements.txt`
- Ensure Python 3.10+ is used.

### Bot not responding or connection issues
- Check your `.env` file for correct API credentials.
- Ensure the bot is added to the group and promoted to admin.

For more help, join the <a href="https://DevilsHeavenMF.t.me">Support group</a>.

<hr>

<div align="center">

⭐ Enjoying the tunes? <b>Star the repo</b> — feedback keeps the rhythm going!

</div>
