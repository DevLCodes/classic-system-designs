# Classic System Design

Interactive pages on how large web systems are built, before any AI is involved: how traffic is spread, data is stored and copied, work is queued, and systems stay correct under load. Every page has a hands-on lab, and every walkthrough has 3D architecture views.

**Start here:** https://devlcodes.github.io/classic-system-designs/

## Building blocks

1. [Non-functional requirements](https://devlcodes.github.io/classic-system-designs/requirements.html)
2. [Network protocols and APIs](https://devlcodes.github.io/classic-system-designs/protocols.html)
3. [DNS](https://devlcodes.github.io/classic-system-designs/dns.html)
4. [Load balancing](https://devlcodes.github.io/classic-system-designs/load-balancing.html)
5. [Rate limiting](https://devlcodes.github.io/classic-system-designs/rate-limiting.html)
6. [Caching](https://devlcodes.github.io/classic-system-designs/caching.html)
7. [Databases, indexes and replication](https://devlcodes.github.io/classic-system-designs/databases.html)
8. [Sharding and consistent hashing](https://devlcodes.github.io/classic-system-designs/sharding.html)
9. [Message queues and streams](https://devlcodes.github.io/classic-system-designs/queues.html)
10. [Consistency and CAP](https://devlcodes.github.io/classic-system-designs/consistency.html)
11. [Consensus with Raft](https://devlcodes.github.io/classic-system-designs/raft.html)
12. [Merkle trees](https://devlcodes.github.io/classic-system-designs/merkle-trees.html)
13. [Cassandra vs CockroachDB](https://devlcodes.github.io/classic-system-designs/cassandra-vs-cockroachdb.html)
14. [Numbers to know](https://devlcodes.github.io/classic-system-designs/numbers.html)

## Worked designs

- [URL shortener](https://devlcodes.github.io/classic-system-designs/url-shortener.html): 100M links a month, 4k–20k redirects/s
- [News feed](https://devlcodes.github.io/classic-system-designs/news-feed.html): 200M daily users, 23k–70k feed loads/s
- [Chat service](https://devlcodes.github.io/classic-system-designs/chat.html): 100M daily users, 25M open connections
- [Distributed rate limiter](https://devlcodes.github.io/classic-system-designs/rate-limiter.html): 1M requests/s across 300 gateways
- [Payments](https://devlcodes.github.io/classic-system-designs/payments.html): 10M payments a day with 10× sale peaks
- [Ride matching](https://devlcodes.github.io/classic-system-designs/ride-matching.html): 5M drivers pinging every 4 s
- [Video streaming](https://devlcodes.github.io/classic-system-designs/video-streaming.html): 500M daily viewers, 26–50 Tb/s of video
- [Live comments](https://devlcodes.github.io/classic-system-designs/live-comments.html): 50M viewers, 11k comments/s
- [Web crawler](https://devlcodes.github.io/classic-system-designs/web-crawler.html): 15B pages in 4 weeks
- [Nearby places](https://devlcodes.github.io/classic-system-designs/nearby-places.html): 500M places, 100k searches/s
- [File sync](https://devlcodes.github.io/classic-system-designs/file-sync.html): files up to 50 GB synced across devices
- [E-commerce store](https://devlcodes.github.io/classic-system-designs/ecommerce.html): 100M daily shoppers with 10× sale days
- [Call insights](https://devlcodes.github.io/classic-system-designs/call-insights.html): 50k recorded sales calls a day, insights in 30 minutes
- [Ticket booking](https://devlcodes.github.io/classic-system-designs/ticket-booking.html): 1M users racing for 50k seats, plus restaurant reservations

The companion site, [agentic system designs](https://devlcodes.github.io/agentic-ai-notebook/system-design/), builds RAG, agents and evals on top of these same blocks.

## Contributing

Plain static HTML with no build step, served by GitHub Pages from `main` (root). Each page inlines its own CSS. The 3D scenes use `assets/scene3d.js` with Three.js 0.160.0 from jsDelivr through an import map. Read [STYLES.md](STYLES.md) before adding or changing a page.
