# Classic System Design

Interactive pages on how large web systems are built, before any AI is involved: how traffic is spread, data is stored and copied, work is queued, and systems stay correct under load. Every page has a hands-on lab, and the six walkthroughs have 3D architecture views.

**Start here:** https://devlcodes.github.io/classic-system-designs/

## Building blocks

1. [Load balancing](https://devlcodes.github.io/classic-system-designs/load-balancing.html)
2. [Rate limiting](https://devlcodes.github.io/classic-system-designs/rate-limiting.html)
3. [Caching](https://devlcodes.github.io/classic-system-designs/caching.html)
4. [Databases, indexes and replication](https://devlcodes.github.io/classic-system-designs/databases.html)
5. [Sharding and consistent hashing](https://devlcodes.github.io/classic-system-designs/sharding.html)
6. [Message queues and streams](https://devlcodes.github.io/classic-system-designs/queues.html)
7. [Consistency and CAP](https://devlcodes.github.io/classic-system-designs/consistency.html)
8. [Numbers to know](https://devlcodes.github.io/classic-system-designs/numbers.html)

## Worked designs

- [URL shortener](https://devlcodes.github.io/classic-system-designs/url-shortener.html): 100M links a month, 4k–20k redirects/s
- [News feed](https://devlcodes.github.io/classic-system-designs/news-feed.html): 200M daily users, 23k–70k feed loads/s
- [Chat service](https://devlcodes.github.io/classic-system-designs/chat.html): 100M daily users, 25M open connections
- [Distributed rate limiter](https://devlcodes.github.io/classic-system-designs/rate-limiter.html): 1M requests/s across 300 gateways
- [Payments](https://devlcodes.github.io/classic-system-designs/payments.html): 10M payments a day with 10× sale peaks
- [Ride matching](https://devlcodes.github.io/classic-system-designs/ride-matching.html): 5M drivers pinging every 4 s

The companion site, [agentic system designs](https://devlcodes.github.io/agentic-ai-notebook/system-design/), builds RAG, agents and evals on top of these same blocks.

## Contributing

Plain static HTML with no build step, served by GitHub Pages from `main` (root). Each page inlines its own CSS. The 3D scenes use `assets/scene3d.js` with Three.js 0.160.0 from jsDelivr through an import map. Read [STYLES.md](STYLES.md) before adding or changing a page.
