# Fedora Core Snap

This repository contains work-in-progress script for constructing a core snap
based on Fedora 24.

# FAQ

Frivolously Anticipated Questions

## What is a core snap?

The core snap is a read-only squashfs filesystem image used as the root
filesystem for snaps based on Fedora RPMs.

## What should be in the core snap?

As little as possible, for now those are essential:

 - the skeleton filesystem
 - the C library
 - bash shell for various wrapper scripts

## Is the fedora-core snap restricted to Fedora?

No, this snap can be used on any distribution where snapd is available. Snaps
that declare to be built against Fedora will simply use the fedora-core snap. A
single system can have snaps from any vendor working alongside each other!

## Can snapd 2.11 use the fedora-core snap?

Not yet, this is still work-in-progress and is not merged upstream.

## I'd like to help, what can I do?

- You can co-maintain snapd packages in Fedora or another distribution
- You can improve the script that builds the core snap, I'd like to shrink it to around 10MB
- You can participate in snapd development to add support for many core snaps
- You can participate in snapcraft development to add support for installing dependencies using libhif
- You can learn about and build snaps!
