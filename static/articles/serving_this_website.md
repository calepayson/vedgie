# How I Built Vedgie Net

### Some Background

I started learning CS by installing Arch Linux (with network manager) on an $80 laptop I named kermit and leaving for Europe. I figured, if I wanted to book train tickets or look up hostels or places to goI would have to learn about computers to do it. 

Little did I know how much I had to learn.

I had no idea a window manager was considered an add on (or even that it was called a window manager), that you needed one to run a browser, and wtf, volume buttons need to be configured??

It was a bit of a trial by fire but it left me with a lingering interest in how computers and operating systems worked.

When I got back I was curious about how computers were networked. To figure it out I took some (very) old mac laptops I found in my parents basement and installed Arch on one (out of comfort) and NixOS on another (NixOS is now my white-whale). 

I did some ssh stuff with them (mind you, I barely knew how to code), was quickly underwhelmed, and decided that, to learn more, I should build a homelab and self-host my own website from it.

I built the website, built the home lab, and then read article after article patiently laying out every reason it was a bad idea to host a public server on your private network as an ameteur.

### The Stack

I host this website on a DigitalOcean droplet for two reasons: It's cheap and it's well documented. 

The droplet I'm using costs only $4 a month and I don't have to worry about some dude in Russia getting up to shenanigans on my local network.

Droplets are also have great official documentation as well as being widely used enough that it's no problem finding a video explenation of any process you're trying.

I use Cloudflare for DNS management and Nginx as a reverse proxy. Again, they're free and well documented.

Vedgie net is a simple FastAPI app that can take markdown documents and serve them as html. To serve the site I run FastAPI with uvicorn and point Nginx to that port. 

### CI/CD

All the code and files are stored on GitHub and I use GitHub Actions to automatically deploy any changes. 

I have a deploy user on the droplet that cannot access the terminal. This user does have a deployer script (pulls any changes and makes sure the FastAPI server is running) that is run whenever a user ssh's in. 

To do auto-deploys I added a very basic GitHub action that, on push, ssh's into the deployer. The deployer runs the script that pulls the changes and makes sure the content is being served.
