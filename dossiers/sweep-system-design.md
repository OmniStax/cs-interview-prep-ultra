# Dossier: sweep of Part V (system design)

Finder run of 2026-11-08. Scope: Part V, with The System Design Primer
(`sdp`, CC BY 4.0) as the registered spine. Alex Xu's book is ruled out, and
no system design prose may be AI-written. So this sweep looks for open,
human-written prose for the topics the primer covers thinly or not at all.
Everything listed here passed or failed the licence gate in
`.claude/agents/resource-finder.md`. Evidence is quoted in
`sources/registry.json` (new rows appended) and repeated in short below.
This dossier does not judge quality.

## 0. How to read this

- **Pins and the no-AI rule.** Several open doc sets are still being edited,
  and some now say so in their own metadata. At HEAD, 19 of the fetched
  Azure Architecture Center pages carry `ai-usage: ai-assisted` front matter,
  for example `patterns/rate-limiting-pattern.md`,
  `patterns/idempotent-consumer.md` and `best-practices/api-implementation.md`.
  Cloudflare's README says "We may use AI tools to help us review technical
  documentation". So every live doc repo is **pinned to its last commit on or
  before 2022-11-30** (azure-arch, mdn, otel, redis-doc, crdb, etcd-site,
  cloudflare-docs, syncthing-docs, k8s-site, aip). At those pins
  azure-arch has no `ai-usage` flags. Exceptions:
  - `citus-docs` added its LICENSE only on 2023-06-28, so it stays at HEAD
    (2025-04-11).
  - The archived AWS repos are pinned to their last commit with content
    (2022-12 to 2023-06).
  - Wikipedia and Wikibooks pages were fetched twice: at the current
    revision and at the last revision before 2022-12-01 (`*.pre2023.*`).
  - Sources written by named authors before the LLM era (Kleppmann,
    Ongaro, AOSA, Bonaventure, Basho/Riak 2.2.3) are pinned at HEAD.
    Peterson and Davie's README carries a "Written by humans, not by AI"
    badge.
- **Product docs.** azure-arch, aws-*, cloudflare-docs, crdb, riak-docs,
  citus-docs, etcd-site and k8s-site describe one vendor's product. The
  general mechanism is usually there, but passages that name products or
  prices need stripping. The licences do not grant trademark rights
  (Cloudflare says so).
- **Locators** follow each registry row's `locator` scheme. Lengths are
  word counts of the cached file (`wc -w`; Markdown, rST or LaTeX source,
  so a little inflated).
- `assumes` lists only prerequisites that the Part V order would put later.
  The concept map isn't built yet, so these are rough and use topic names.

## 1. Per-topic coverage

Primer coverage: **full** means a section that explains the idea with its
trade-offs; **thin** means under about 50 lines, or only a definition and a
pros/cons list; **none** means no section, at most a mention or a link.

| Topic | Primer (sdp) | Primer locator | Open candidates found (source ids; details in §2) |
|---|---|---|---|
| Scaling step by step (1 server → millions) | full | sdp:solutions/scaling_aws; sdp:#how-to-approach-a-system-design-interview-question | aosa:v2/distsys (Matsudaira: caches, proxies, indexes, LBs, queues); azure-arch:guide/design-principles/scale-out, guide/architecture-styles/{n-tier,web-queue-worker}; azure-arch:best-practices/auto-scaling; k8s-site HPA; wp:Scalability, wp:Autoscaling |
| DNS | thin (39 lines) | sdp:#domain-name-system | cnp3:protocols/dns, cnp3:principles/naming (+ exercises/dns); aws-route53:welcome-dns-service, routing-policy-*, dns-failover; wb:Communication_Networks/DNS; wp:Domain_Name_System, Round-robin_DNS, Anycast, Time_to_live; mdn:glossary/dns; sysapproach:applications/infrastructure (licence unclear) |
| CDN | thin (42 lines) | sdp:#content-delivery-network | cloudflare-docs:reference-architecture/cdn-reference-architecture (3.4k words), cache/about/*; aws-cloudfront:HowCloudFrontWorks, Expiration, cache-hit-ratio; azure-arch:best-practices/cdn; wb:Routing_protocols_and_architectures/Content_Delivery_Networks; wp:Content_delivery_network; mdn:glossary/cdn; sysapproach:applications/overlays (unclear) |
| Load balancing | full (71 lines) | sdp:#load-balancer | aws-elb:introduction, sticky-sessions, target-group-health-checks; cloudflare-docs:load-balancing/understand-basics/*; azure-arch:guide/technology-choices/load-balancing-overview; k8s-site:concepts/services-networking/service; aosa:v2/distsys#1.3; aosa:v2/nginx; wp:Load_balancing_(computing) (5.9k words) |
| Reverse proxies | thin (44 lines) | sdp:#reverse-proxy-web-server | mdn:web/http/proxy_servers_and_tunneling; aosa:v2/nginx; azure-arch:patterns/gateway-offloading, gateway-routing; wp:Reverse_proxy; wb:Internet_Technologies/Proxy_servers (179 words) |
| Caching strategies | full | sdp:#cache, sdp:#when-to-update-the-cache | aws-elasticache:redis/Strategies (lazy loading, write-through, TTL); azure-arch:best-practices/caching (11k words), patterns/cache-aside, antipatterns/no-caching; mdn:web/http/caching (5.1k words); cloudflare-docs:cache/about/*; redis-doc:docs/reference/eviction; wp:Cache_(computing), Cache_replacement_policies, Cache_stampede, Thundering_herd_problem, Cache_invalidation |
| SQL vs NoSQL | full | sdp:#sql-or-nosql | aosa:v1/nosql (Adam Marcus, 9.7k words); azure-arch:guide/technology-choices/data-store-overview, data-guide/big-data/non-relational-data; riak-docs:learn/new-to-nosql; wp:NoSQL, Relational_database, ACID, Key–value_database, Wide-column_store, Document-oriented_database |
| Replication | full (leader-based only) | sdp:#replication, sdp:#master-slave-replication | kleppmann-ds:sec:replication, sec:broadcast-replication; riak-docs:learn/concepts/replication; crdb:v22.2/architecture/replication-layer; redis-doc:docs/management/replication; wb:PostgreSQL/Replication, MySQL/Replication; wp:Replication_(computing), Multi-master_replication |
| Sharding / partitioning | thin (29 lines) | sdp:#sharding | azure-arch:patterns/sharding (3.9k), best-practices/data-partitioning (+ -strategies); aws-dynamodb:HowItWorks.Partitions, bp-partition-key-design, bp-partition-key-sharding; citus-docs:sharding/data_modeling, get_started/concepts; crdb:v22.2/architecture/distribution-layer; redis-doc:docs/reference/cluster-spec (hash slots); wp:Shard_(database_architecture), Partition_(database) |
| Consistent hashing | **none** (links only, sdp:#sharding) | — | wp:Consistent_hashing, Rendezvous_hashing, Distributed_hash_table, Chord_(peer-to-peer), Kademlia; riak-docs:learn/concepts/clusters (ring), vnodes; aosa:v1/riak; sysapproach:applications/overlays (consistent hashing for CDN URL→server, licence unclear); arxiv papers link-only (jump hash, bounded loads) |
| CAP and consistency models | thin (62 lines) | sdp:#availability-vs-consistency, sdp:#consistency-patterns | kleppmann-ds:sec:linearizability, sec:eventual-consistency, sec:consistency; arxiv-consistency-survey (52 pp.); etcd-site:v3.5/learning/api_guarantees; riak-docs:learn/concepts/eventual-consistency, strong-consistency; aws-dynamodb:HowItWorks.ReadConsistency; wp:CAP_theorem, PACELC_design_principle, Consistency_model (6.9k), Linearizability, Eventual_consistency, Database_transaction_schedule (Serializability redirects here), Isolation_(database_systems), Snapshot_isolation |
| Quorums | **none** | — | kleppmann-ds:sec:quorums; riak-docs:developing/app-guide/replication-properties (N/R/W, PR/PW), learn/concepts/replication; arxiv-relaxed-paxos; wp:Quorum_(distributed_computing); raft-thesis (majority quorums) |
| Consensus (Paxos, Raft, leader election) | none (one Raft link) | — | raft-thesis (whole dissertation); raft-site:index.html; kleppmann-ds:sec:consensus; aosa:500L/clustering-by-consensus (Paxos, with code); crdb:v22.2/architecture/replication-layer; azure-arch:patterns/leader-election; wp:Paxos_(computer_science), Raft_(algorithm), Consensus_(computer_science), Leader_election, Two-phase_commit_protocol, State_machine_replication, Split-brain_(computing) |
| Message queues and back-pressure | thin (47 lines incl. task queues and back pressure) | sdp:#asynchronism, sdp:#back-pressure | aws-sqs:standard-queues, sqs-visibility-timeout, FIFO-queues-exactly-once-processing, sqs-dead-letter-queues, sqs-short-and-long-polling; azure-arch:patterns/queue-based-load-leveling, competing-consumers, publisher-subscriber, priority-queue, guide/technology-choices/messaging (3.6k); cloudflare-docs:queues/learning/{delivery-guarantees,batching-retries}; aosa:v2/zeromq; wp:Message_queue, Message_broker, Publish–subscribe_pattern, Dead_letter_queue, Backpressure_routing (network sense), Little's_law, Queueing_theory, M/M/1_queue |
| Rate limiting (token bucket, leaky bucket) | **none** (one link to Stripe blog) | sdp:#additional-system-design-interview-questions | wp:Token_bucket, Leaky_bucket (6.6k), Generic_cell_rate_algorithm, Rate_limiting; redis-doc:commands/incr#pattern-rate-limiter (two implementations); aws-apigw:api-gateway-request-throttling (token bucket); azure-arch:patterns/rate-limiting-pattern, throttling; cloudflare-docs:waf/rate-limiting-rules; mdn:web/http/status/429, headers/retry-after; redis-cell (MIT code, GCRA); sysapproach:congestion/qos (token bucket filter, licence unclear) |
| Unique ID generation | **none** (one link to Snowflake) | sdp:#additional-system-design-interview-questions | wp:Snowflake_ID (510 words), Universally_unique_identifier, Unix_time; sonyflake (MIT code + README); ksuid (MIT code + README). Thin: no open prose that compares the designs (auto-increment with offsets, ticket server, UUID, Snowflake). |
| Back-of-envelope estimation | thin (section is links; worked numbers in each solution) | sdp:#back-of-the-envelope-calculations, sdp:#powers-of-two-table, worked examples in sdp:solutions/*#step-1 | wp:Fermi_problem, Back-of-the-envelope_calculation; latency-colin (MIT, latency model by year); azure-arch:best-practices/auto-scaling (capacity); wp:Little's_law. Thin: no open worked-estimation prose besides the primer's own solutions. |
| Latency numbers | full (table) | sdp:#latency-numbers-every-programmer-should-know | latency-colin (MIT code: extrapolated numbers by year); wp:Latency_(engineering); mdn:glossary/latency, glossary/bandwidth; sysapproach:foundation/performance (unclear) |
| Idempotency | **none** (HTTP verb table column only) | sdp:#hypertext-transfer-protocol-http | aip:0155 (request IDs), aip:0194 (retries); mdn:glossary/idempotent, web/http/methods/*; azure-arch:patterns/retry, competing-consumers, best-practices/api-design#idempotent; aws-sqs:FIFO-queues-exactly-once-processing; aws-sns:fifo-message-dedup; raft-thesis:clients (linearizable semantics via client sessions); wp:Idempotence (CS section) |
| Observability | **none** ("monitoring" appears only as a bullet in solutions) | — | otel:observability-primer, signals/{traces,metrics,logs,baggage}; azure-arch:best-practices/monitoring (14k words), patterns/health-endpoint-monitoring; aosa:v1/graphite; wp:Observability_(software), Tracing_(software), Service-level_objective, Service_level_indicator, Service-level_agreement, Site_reliability_engineering |
| Case: URL shortener | full | sdp:solutions/pastebin | wp:URL_shortening, Base64, Pastebin. |
| Case: news feed | full | sdp:solutions/twitter | redis-doc:docs/manual/patterns/twitter-clone (4.3k words: fan-out on write with Redis lists); wp:Web_feed (the "News feed" title redirects there; it is about RSS-style feeds) |
| Case: chat | **none** | — | mdn:web/api/websockets_api, web/api/server-sent_events; wp:Instant_messaging, XMPP, WebSocket, Push_technology, Comet_(programming), Server-sent_events, Push_technology#Long_polling; kleppmann-ds:sec:broadcast (ordering), sec:causality. Thin: no open end-to-end chat design. |
| Case: notification system | **none** | — | aws-sns:sns-common-scenarios (fan-out), sns-message-delivery-retries, mobile-push-notifications*; azure-arch:patterns/publisher-subscriber, priority-queue; wp:Push_technology, Apple_Push_Notification_service, Firebase_Cloud_Messaging. Thin: product docs only. |
| Case: web crawler | full | sdp:solutions/web_crawler | aosa:500L/a-web-crawler-with-asyncio-coroutines (8.2k words, with code); wp:Web_crawler, Robots.txt, Focused_crawler, Spider_trap, URI_normalization, Sitemaps |
| Case: key-value store | thin (sdp:solutions/query_cache is a cache, not a store) | sdp:solutions/query_cache | riak-docs:learn/concepts/* (whole Dynamo-style design); kleppmann-ds (replication, quorums, eventual consistency); aosa:v1/riak, v1/bdb, 500L/dbdb; cloudflare-docs:workers/learning/how-kv-works; etcd-site:v3.5/learning/why; tinykv (code exercise with tests); wp:Dynamo_(storage_system), Bigtable, Log-structured_merge-tree, Write-ahead_logging, Merkle_tree, Vector_clock, Gossip_protocol, Bloom_filter |
| Case: search autocomplete | **none** | — | wp:Autocomplete, Trie, Count–min_sketch, Inverted_index, Search_engine_indexing; ods/cpa tries already registered (DSA side). Thin: no open system-level design. arXiv CC BY items are ML ranking papers (e.g. 2411.04129 AmazonQAC dataset), off-scope for interview prose. |
| Case: video streaming | **none** | — | mdn:web/media/dash_adaptive_streaming_for_html_5_video, web/guide/audio_and_video_delivery/{setting_up_adaptive_streaming_media_sources,live_streaming_web_audio_and_video}; wp:Adaptive_bitrate_streaming, HTTP_Live_Streaming, Dynamic_Adaptive_Streaming_over_HTTP, Transcoding, Video_on_demand; cloudflare-docs CDN reference architecture; sysapproach:data/multimedia#adaptive-streaming (unclear) |
| Case: file sync | **none** | — | syncthing-docs:specs/bep-v1 (4.9k words: blocks, hashes, index exchange, version vectors), users/syncing, users/versioning; wp:File_synchronization, Rsync, Delta_encoding, Merkle_tree, Data_deduplication, Content-addressable_storage; aosa:v1/hdfs |

### Topics still without open prose that reads like a design

These have open material on the mechanisms but nothing open that walks
through the design, with requirements, estimates and a diagram, the way the
primer's solutions do:

- **Chat system**, **notification system**, **search autocomplete**,
  **video streaming**, **file sync**: only mechanisms (protocol specs,
  product docs, Wikipedia). Syncthing's BEP is the closest to a real design.
- **Unique ID generation**: only Wikipedia's short Snowflake article and two
  MIT-licensed READMEs (code-only under the gate). There is no comparison
  of approaches.
- **Back-of-envelope estimation**: nothing open beyond the primer's
  solutions and Wikipedia's Fermi article.
- **Rate limiting as a distributed design** (counters shared across nodes,
  sliding-window log vs counter): there are algorithm articles and short
  product pages. The Redis INCR pattern is the only open implementation
  walkthrough.

## 2. Candidates

Kinds: prose | code-exercise | exercise | figure | dataset | transcript |
link-only. `nc` is false for every row (no NC item here passes for prose).

### 2.1 Open textbooks, lecture notes, dissertations

| locator | source id | licence | nc | kind | concepts covered | length | assumes | what it is |
|---|---|---|---|---|---|---|---|---|
| kleppmann-ds:sec:introduction … sec:availability | kleppmann-ds | CC BY-SA 4.0 | false | prose | why distribute, networking latency/bandwidth, availability, SLOs, fault tolerance | ~4k (lines 47-568) | — | Intro of Kleppmann's Cambridge notes, prose around embedded slides |
| kleppmann-ds:sec:rpc | kleppmann-ds | CC BY-SA 4.0 | false | prose | RPC, retries, idempotence of requests | ~2.3k | — | RPC example incl. what happens on retry |
| kleppmann-ds:sec:system-models, sec:two-generals, sec:byzantine, sec:failure-detectors | kleppmann-ds | CC BY-SA 4.0 | false | prose | system models, timeouts, failure detection | ~7k | — | Two generals, Byzantine generals, network/node/timing models |
| kleppmann-ds:sec:time … sec:logical-time | kleppmann-ds | CC BY-SA 4.0 | false | prose | physical clocks, NTP, happens-before, Lamport and vector clocks | ~12k | — | Time and ordering; useful for unique IDs (timestamps) and KV versioning |
| kleppmann-ds:sec:broadcast | kleppmann-ds | CC BY-SA 4.0 | false | prose | FIFO/causal/total-order broadcast | ~7k | logical clocks | Delivery orders and algorithms (chat ordering) |
| kleppmann-ds:sec:replication, sec:remote-state, sec:quorums, sec:broadcast-replication | kleppmann-ds | CC BY-SA 4.0 | false | prose + figure (TikZ) | replication, idempotence, read repair, quorums (r+w>n) | ~7k | — | Replication from first principles, with the quorum condition |
| kleppmann-ds:sec:consistency, sec:2pc, sec:linearizability | kleppmann-ds | CC BY-SA 4.0 | false | prose | 2PC, linearizability, ABD | ~7k | quorums | Replica consistency |
| kleppmann-ds:sec:consensus (incl. Raft subsection) | kleppmann-ds | CC BY-SA 4.0 | false | prose + pseudocode | consensus, FLP, Raft | ~8k | replication | Consensus and total order broadcast with Raft pseudocode |
| kleppmann-ds:sec:eventual-consistency, sec:collaboration | kleppmann-ds | CC BY-SA 4.0 | false | prose | eventual consistency, CAP, CRDTs, collaborative editing | ~9k | — | Eventual consistency, CAP discussion, CRDTs |
| kleppmann-ds:ex1 … ex25 (solutions.tex) | kleppmann-ds | CC BY-SA 4.0 | false | exercise | all of the above | 25 exercises | — | Supervision exercises; solution notes build from the same source |
| raft-thesis:basicraft/* | raft-thesis | CC BY 3.0 US / 4.0 | false | prose + figure | Raft leader election, log replication, safety | ~25k (chapter) | — | Basic Raft chapter (paper content, licensed with Ousterhout's permission) |
| raft-thesis:clients/* | raft-thesis | CC BY 3.0 US / 4.0 | false | prose | linearizable semantics, client sessions, duplicate detection (idempotency) | chapter | Raft basics | Client interaction chapter |
| raft-thesis:membership, leaderelection, compaction, motivation | raft-thesis | CC BY 3.0 US / 4.0 | false | prose | membership change, election timing, log compaction, replicated state machines | chapters | Raft basics | Remaining chapters |
| raft-site:index.html | raft-site | CC BY 3.0 | false | prose | Raft overview | ~2k | — | Website overview text (raft.pdf in the repo excluded: paper has no licence) |
| aosa:v2/distsys | aosa | CC BY 3.0 | false | prose + figure | scaling step by step, caches, proxies, indexes, load balancers, queues | 7.9k | — | Kate Matsudaira, "Scalable Web Architecture and Distributed Systems" |
| aosa:v1/nosql | aosa | CC BY 3.0 | false | prose | SQL vs NoSQL, data models, consistency, partitioning, consistent hashing | 9.7k | consistent hashing | Adam Marcus, "The NoSQL Ecosystem" |
| aosa:v1/riak | aosa | CC BY 3.0 | false | prose | Riak/Erlang design, ring | 7.4k | — | Riak and Erlang/OTP (more Erlang than KV design) |
| aosa:v1/hdfs | aosa | CC BY 3.0 | false | prose | distributed file system, replication, blocks | 6.9k | replication | HDFS chapter |
| aosa:v2/nginx | aosa | CC BY 3.0 | false | prose | reverse proxy, event-driven server, load balancing | 7.0k | — | nginx architecture |
| aosa:v1/graphite | aosa | CC BY 3.0 | false | prose | metrics storage, observability | 4.9k | — | Graphite metrics system |
| aosa:v2/zeromq | aosa | CC BY 3.0 | false | prose | messaging patterns, queues | 6.2k | — | ZeroMQ design |
| aosa:v1/bdb | aosa | CC BY 3.0 | false | prose | embedded KV store, WAL, transactions | 9.5k | — | Berkeley DB |
| aosa:posa/infinispan | aosa | CC BY 3.0 | false | prose | distributed cache performance | 3.2k | — | Infinispan (POSA) |
| aosa:posa/high-performance-networking-in-chrome | aosa | CC BY 3.0 | false | prose | latency, DNS prefetch, TCP, caching | 8.1k | — | Ilya Grigorik, Chrome networking |
| aosa:500L/a-web-crawler-with-asyncio-coroutines | aosa | CC BY 3.0 (code: check chapter) | false | prose + code | web crawler, concurrency | 8.2k | — | Jesse Jiryu Davis and Guido van Rossum, crawler built step by step |
| aosa:500L/clustering-by-consensus | aosa | CC BY 3.0 (code: check chapter) | false | prose + code + figure | Paxos, replicated state machine | 8.5k | — | Dustin Mitchell, Multi-Paxos cluster in Python |
| aosa:500L/dbdb-dog-bed-database | aosa | CC BY 3.0 (code: check chapter) | false | prose + code | KV store on disk, immutable tree | 3.9k | — | Taavi Burns, tiny KV database |
| cnp3:protocols/dns, cnp3:principles/naming | cnp3 | CC BY 3.0 / CC BY-SA 3.0 (per file) | false | prose | DNS, naming, resolvers, caching | 1.5k + 3.1k | — | Bonaventure's open networking book |
| cnp3:protocols/http, protocols/http2 | cnp3 | CC BY 3.0 | false | prose | HTTP, caching headers, persistent connections | 5.6k + | — | HTTP chapter |
| cnp3:protocols/rpc | cnp3 | CC BY-SA 3.0 | false | prose | RPC | — | — | RPC chapter |
| cnp3:exercises/dns, exercises/http | cnp3 | CC BY 3.0 | false | exercise | DNS, HTTP | 1.0k + 0.7k | — | Unkeyed exercises |
| arxiv-consistency-survey:1-7 | arxiv-consistency-survey | CC BY 4.0 | false | prose | consistency models (strict, sequential, causal, eventual, client-centric) | 52 pp. | — | Survey paper |
| arxiv-relaxed-paxos:1-5 | arxiv-relaxed-paxos | CC BY 4.0 | false | prose | quorum intersection, Paxos | 8 pp. | Paxos | Research paper by Howard and Mortier |

### 2.2 Open documentation sets (product docs, pinned pre-2023)

| locator | source id | licence | nc | kind | concepts covered | length | assumes | what it is |
|---|---|---|---|---|---|---|---|---|
| azure-arch:patterns/sharding | azure-arch | CC BY 4.0 | false | prose + figure | sharding strategies (lookup, range, hash), rebalancing, hotspots | 3.9k | — | Sharding pattern |
| azure-arch:best-practices/data-partitioning, data-partitioning-strategies | azure-arch | CC BY 4.0 | false | prose + figure | horizontal/vertical/functional partitioning | 3.7k + 6.6k | — | Data partitioning guidance (deleted from HEAD later) |
| azure-arch:patterns/rate-limiting-pattern, throttling | azure-arch | CC BY 4.0 | false | prose | rate limiting, throttling, back-pressure, queues as buffers | 2.2k + 1.7k | queues | At the pin, neither page names token or leaky bucket (HEAD's throttling.md adds a table of them) |
| azure-arch:patterns/cache-aside; best-practices/caching; antipatterns/no-caching | azure-arch | CC BY 4.0 | false | prose + figure | cache-aside, expiry, eviction, consistency, distributed caching | 1.6k / 11.2k / 2.0k | — | Caching guidance |
| azure-arch:best-practices/cdn | azure-arch | CC BY 4.0 | false | prose | CDN uses, challenges | 1.8k | — | CDN guidance |
| azure-arch:patterns/queue-based-load-leveling, competing-consumers, publisher-subscriber, priority-queue | azure-arch | CC BY 4.0 | false | prose + figure | queues, load levelling, idempotent consumers, pub/sub | 1.1k-1.9k each | — | Messaging patterns |
| azure-arch:guide/technology-choices/messaging | azure-arch | CC BY 4.0 | false | prose | commands vs events, at-least-once, ordering, dedup | 3.6k | — | Messaging technology overview |
| azure-arch:patterns/retry, circuit-breaker; antipatterns/retry-storm; best-practices/transient-faults | azure-arch | CC BY 4.0 | false | prose | retries, backoff, idempotency, circuit breakers | 2.2k / 3.5k / 1.3k / 3.9k | — | Resilience patterns |
| azure-arch:patterns/leader-election | azure-arch | CC BY 4.0 | false | prose | leader election (lease/lock based) | 2.3k | — | Leader election pattern |
| azure-arch:patterns/health-endpoint-monitoring; best-practices/monitoring | azure-arch | CC BY 4.0 | false | prose + figure | health checks, telemetry pipeline, alerting | 2.3k / 14.1k | — | Monitoring guidance |
| azure-arch:best-practices/api-design | azure-arch | CC BY 4.0 | false | prose | REST design, idempotent PUT, pagination | 6.1k | — | API design |
| azure-arch:best-practices/auto-scaling; guide/design-principles/{scale-out,partition}; guide/architecture-styles/{n-tier,web-queue-worker} | azure-arch | CC BY 4.0 | false | prose | horizontal scaling, autoscaling, tiers | 3.4k / 0.6k / 0.6k / 0.8k | — | Scaling principles |
| azure-arch:guide/technology-choices/load-balancing-overview | azure-arch | CC BY 4.0 | false | prose | global vs regional, L4 vs L7 load balancing | 1.7k | — | Load balancing overview (Azure-specific in parts) |
| azure-arch:guide/technology-choices/data-store-overview; data-guide/big-data/non-relational-data | azure-arch | CC BY 4.0 | false | prose | relational vs KV/document/columnar/graph | 2.8k / 2.7k | — | Data store models |
| aws-elasticache:redis/Strategies | aws-elasticache | CC BY-SA 4.0 | false | prose + code | lazy loading, write-through, TTL | 1.4k | — | Caching strategies page |
| aws-apigw:api-gateway-request-throttling | aws-apigw | CC BY-SA 4.0 | false | prose | token bucket throttling, burst vs rate | 0.7k | — | Throttling page |
| aws-sqs:standard-queues, sqs-visibility-timeout, FIFO-queues-exactly-once-processing, sqs-dead-letter-queues, sqs-short-and-long-polling | aws-sqs | CC BY-SA 4.0 | false | prose | at-least-once, visibility timeout, dedup, DLQ, polling | 0.1k-2.0k each | — | SQS guide pages |
| aws-sns:sns-common-scenarios, sns-message-delivery-retries, fifo-message-dedup, mobile-push-notifications* | aws-sns | CC BY-SA 4.0 | false | prose | fan-out, retry policy/backoff, dedup, push | 0.5k / 1.2k / 0.4k | queues | SNS guide pages |
| aws-dynamodb:HowItWorks.Partitions, HowItWorks.ReadConsistency, bp-partition-key-design, bp-partition-key-sharding | aws-dynamodb | CC BY-SA 4.0 | false | prose + figure | hash partitioning, hot keys, write sharding, eventual vs strong reads | 0.4k-0.9k each | — | DynamoDB pages |
| aws-cloudfront:HowCloudFrontWorks, Expiration, cache-hit-ratio | aws-cloudfront | CC BY-SA 4.0 | false | prose | CDN request flow, TTLs, cache hit ratio | 1.0k / 1.7k / 1.3k | — | CloudFront pages |
| aws-route53:welcome-dns-service, routing-policy*, dns-failover* | aws-route53 | CC BY-SA 4.0 | false | prose | how DNS resolution works, latency/geo/weighted routing, failover | 0.9k + many short pages | — | Route 53 pages |
| aws-elb:introduction, sticky-sessions, target-group-health-checks | aws-elb | CC BY-SA 4.0 | false | prose | L7 LB, listeners, health checks, sticky sessions | 1.4k / 1.8k / 1.6k | — | ALB guide pages |
| cloudflare-docs:reference-architecture/cdn-reference-architecture | cloudflare-docs | CC BY 4.0 | false | prose + figure | CDN architecture, anycast, tiered cache | 3.4k | — | CDN reference architecture |
| cloudflare-docs:cache/about/* | cloudflare-docs | CC BY 4.0 | false | prose | cache keys, TTLs, tiered cache, Cache-Control | 0.3k-1.0k each | — | Cache concept pages |
| cloudflare-docs:load-balancing/understand-basics/* | cloudflare-docs | CC BY 4.0 | false | prose | pools, monitors, steering, session affinity | short pages | — | LB concept pages |
| cloudflare-docs:waf/rate-limiting-rules/* | cloudflare-docs | CC BY 4.0 | false | prose | rate limiting rules, counting characteristics | 0.7k + | — | Rate limiting rules |
| cloudflare-docs:queues/learning/{how-queues-works,delivery-guarantees,batching-retries} | cloudflare-docs | CC BY 4.0 | false | prose | at-least-once, batching, retries | 0.3k-0.5k | — | Queues concept pages |
| cloudflare-docs:workers/learning/how-kv-works | cloudflare-docs | CC BY 4.0 | false | prose | eventually consistent global KV, edge caching | 0.5k | — | KV concept page |
| mdn:web/http/caching | mdn | CC BY-SA 2.5 | false | prose | HTTP caching, freshness, validation, shared/private caches | 5.1k | — | HTTP caching guide |
| mdn:web/http/proxy_servers_and_tunneling | mdn | CC BY-SA 2.5 | false | prose | forward vs reverse proxy | 0.8k | — | Proxy guide |
| mdn:web/http/status/429; headers/retry-after; headers/cache-control | mdn | CC BY-SA 2.5 | false | prose | rate limit signalling, caching headers | short | — | Reference pages |
| mdn:glossary/idempotent; web/http/methods/* | mdn | CC BY-SA 2.5 | false | prose | idempotent and safe methods | 0.3k + | — | Glossary and method pages |
| mdn:web/api/websockets_api, web/api/server-sent_events/* | mdn | CC BY-SA 2.5 | false | prose + code | WebSockets, SSE (chat, notifications) | 0.6k / 1.3k | — | Real-time web APIs |
| mdn:web/media/dash_adaptive_streaming_for_html_5_video; web/guide/audio_and_video_delivery/{setting_up_adaptive_streaming_media_sources,live_streaming_web_audio_and_video} | mdn | CC BY-SA 2.5 | false | prose | DASH/HLS, adaptive bitrate | 0.7k / 1.5k / 1.6k | — | Streaming guides |
| mdn:glossary/{cdn,dns,latency,bandwidth,cache,proxy_server} | mdn | CC BY-SA 2.5 | false | prose | definitions | tiny | — | Glossary entries |
| otel:observability-primer; otel:signals/{traces,metrics,logs,baggage} | otel | CC BY 4.0 | false | prose | observability, SLIs/SLOs, distributed tracing, spans | 0.9k / 1.7k / 0.4k / 0.1k / 0.4k | — | OpenTelemetry concepts |
| redis-doc:commands/incr#pattern-rate-limiter | redis-doc | CC BY-SA 4.0 | false | prose + pseudocode | fixed-window counters, race conditions | ~0.6k of 0.9k | — | Two rate limiter implementations with INCR/EXPIRE |
| redis-doc:docs/manual/patterns/twitter-clone | redis-doc | CC BY-SA 4.0 | false | prose + code | news feed: posts, followers, timelines (fan-out on write) | 4.3k | — | Building a Twitter clone with Redis |
| redis-doc:docs/manual/patterns/distributed-locks | redis-doc | CC BY-SA 4.0 | false | prose | distributed locks (Redlock) | 3.3k | — | Redlock description (contested design; Kleppmann's critique is a blog, link-only) |
| redis-doc:docs/management/replication | redis-doc | CC BY-SA 4.0 | false | prose | async leader-follower replication | 4.2k | — | Redis replication |
| redis-doc:docs/reference/cluster-spec | redis-doc | CC BY-SA 4.0 | false | prose | hash slots, resharding, gossip, failover | 13.8k | sharding | Redis Cluster spec |
| redis-doc:docs/reference/eviction | redis-doc | CC BY-SA 4.0 | false | prose | LRU/LFU approximations | short | — | Eviction policies |
| riak-docs:learn/concepts/{clusters,vnodes,replication,eventual-consistency,strong-consistency,active-anti-entropy,causal-context,crdts} | riak-docs | CC BY 4.0 | false | prose + figure | ring/consistent hashing, vnodes, N/R/W, read repair, Merkle-tree AAE, vector clocks | 0.7k-2.0k each (~10k total) | — | Dynamo-style KV concepts |
| riak-docs:developing/app-guide/replication-properties | riak-docs | CC BY 4.0 | false | prose | quorums (N, R, W, PR, PW, DW), sloppy quorum | 3.8k | replication | Replication properties guide |
| riak-docs:developing/usage/conflict-resolution | riak-docs | CC BY 4.0 | false | prose | siblings, last-write-wins, conflict resolution | 3.4k | vector clocks | Conflict resolution |
| crdb:v22.2/architecture/{overview,replication-layer,distribution-layer,transaction-layer} | crdb | CC BY 4.0 | false | prose | Raft per range, leaseholders, range-based sharding, splits, rebalancing | 1.0k / 3.0k / 2.4k / … | Raft | CockroachDB architecture |
| etcd-site:v3.5/learning/{why,api_guarantees} | etcd-site | CC BY 4.0 | false | prose | linearizable vs serializable reads, consensus-backed KV | 2.2k / 0.7k | Raft | etcd learning pages |
| citus-docs:get_started/concepts; sharding/data_modeling | citus-docs | CC BY 4.0 | false | prose | distribution column, co-location, reference tables | 2.3k / 2.8k | — | Sharding Postgres |
| syncthing-docs:specs/bep-v1; users/{syncing,versioning,faq} | syncthing-docs | CC BY 4.0 | false | prose | file sync protocol: blocks, hashes, index updates, version vectors, conflicts | 4.9k / 1.2k / … | vector clocks | Block Exchange Protocol |
| k8s-site:concepts/services-networking/service; tasks/run-application/horizontal-pod-autoscale | k8s-site | CC BY 4.0 | false | prose | service discovery, L4 LB, autoscaling algorithm | 6.5k / 4.0k | — | Kubernetes pages |
| aip:0155, 0194, 0193, 0158 | aip | CC BY 4.0 | false | prose (normative) | idempotency via request IDs, retry rules, errors, pagination | 0.5k / 0.6k / 0.5k / 1.2k | — | Google AIPs |
| wb:Routing_protocols_and_architectures/Content_Delivery_Networks | wb-sysdesign | CC BY-SA | false | prose | CDN, request routing | 1.1k | — | Wikibooks (Politecnico di Torino course notes) |
| wb:Communication_Networks/DNS; Communication_Networks/HTTP_Protocol | wb-sysdesign | CC BY-SA | false | prose | DNS, HTTP | 4.8k / 3.3k | — | Wikibooks |
| wb:PostgreSQL/Replication; MySQL/Replication; Oracle_and_DB2…/Replication | wb-sysdesign | CC BY-SA | false | prose | DB replication modes | 2.5k / 1.1k / 0.5k | — | Wikibooks |
| wb:The_World_of_Peer-to-Peer_(P2P)/Building_a_P2P_System | wb-sysdesign | CC BY-SA | false | prose | DHTs, P2P overlays | 11.5k | — | Wikibooks |

### 2.3 Code, datasets, code exercises

| locator | source id | licence | nc | kind | concepts covered | length | assumes | what it is |
|---|---|---|---|---|---|---|---|---|
| latency-colin:interactive_latency.html | latency-colin | MIT | false | dataset | latency numbers by year | 1 file | — | JS model behind the "latency numbers by year" page |
| sonyflake:sonyflake.go | sonyflake | MIT | false | code (README is MIT prose: code-only) | Snowflake-style IDs | small | — | Go ID generator |
| ksuid:ksuid.go | ksuid | MIT | false | code (README code-only) | sortable random IDs | small | — | Go ID generator |
| redis-cell:src/cell/* | redis-cell | MIT | false | code | GCRA / token bucket | small | — | Rust rate limiter |
| tinykv:doc/project1..4 + tests | tinykv | Apache 2.0 | false | code-exercise | standalone KV, Raft KV, multi-Raft sharding, transactions | 4 projects | Raft | Course project with test suites (statement prose is Apache: needs a ruling) |
| exercism:rest-api, exercism:circular-buffer | exercism (registered) | MIT | false | code-exercise | REST API state, bounded buffer (back-pressure analogue) | — | — | Already registered; marginal fit |

### 2.4 Wikipedia (CC BY-SA 4.0), fetched to `sources/_cache/wp-sysdesign/`

Each row is `wp:<title>`, kind prose, nc false, with no `assumes` listed. The
length is the rendered-text word count at the current revision.
`revid_pre2023` is the last revision before 2022-12-01, fetched as
`<title>.pre2023.{txt,wiki}`.

| article | revid (current) | revid_pre2023 (date) | words |
|---|---|---|---|
| wp:ACID | 1381669262 | 1124557260 (09:10, 29 November 2022) | 1936 |
| wp:Adaptive_bitrate_streaming | 1383584032 | 1120818982 (00:14, 9 November 2022) | 4382 |
| wp:Anycast | 1384017898 | 1114166620 (04:38, 5 October 2022) | 1495 |
| wp:Apache_Cassandra | 1381293162 | 1123203054 (14:20, 22 November 2022) | 2197 |
| wp:Apache_Kafka | 1382882648 | 1116578283 (08:15, 17 October 2022) | 901 |
| wp:Apache_ZooKeeper | 1346340908 | 1106535869 (03:29, 25 August 2022) | 755 |
| wp:API_management | 1379737129 | 1076099310 (10:16, 9 March 2022) | 794 |
| wp:Apple_Push_Notification_service | 1383391602 | 1124585727 (13:16, 29 November 2022) | 857 |
| wp:Autocomplete | 1383224442 | 1118483615 (07:14, 27 October 2022) | 3795 |
| wp:Autoscaling | 1384315884 | 1071395594 (11:27, 12 February 2022) | 2052 |
| wp:Back-of-the-envelope_calculation | 1376805115 | 1088038676 (21:39, 15 May 2022) | 1292 |
| wp:Backpressure_routing | 1333463650 | 1045657229 (18:42, 21 September 2021) | 4984 |
| wp:Base64 | 1382521149 | 1124762714 (10:29, 30 November 2022) | 3643 |
| wp:Bigtable | 1376009623 | 1121149749 (19:38, 10 November 2022) | 1456 |
| wp:BitTorrent | 1383549646 | 1119883374 (22:59, 3 November 2022) | 9417 |
| wp:Bloom_filter | 1381027200 | 1122201044 (10:40, 16 November 2022) | 10207 |
| wp:Byzantine_fault | 1381560430 | 1121559471 (23:16, 12 November 2022) | 3974 |
| wp:Cache_(computing) | 1377581139 | 1123536428 (07:52, 24 November 2022) | 3533 |
| wp:Cache_invalidation | 1188797099 | 1049478470 (02:10, 12 October 2021) | 466 |
| wp:Cache_replacement_policies | 1376205644 | 1114056358 (15:29, 4 October 2022) | 3821 |
| wp:Cache_stampede | 1330515031 | 1075757765 (14:26, 7 March 2022) | 1007 |
| wp:CAP_theorem | 1382061767 | 1115687117 (17:56, 12 October 2022) | 797 |
| wp:Chord_(peer-to-peer) | 1371957200 | 1121298044 (15:28, 11 November 2022) | 2199 |
| wp:Circuit_breaker_design_pattern | 1373541062 | 1121366083 (22:34, 11 November 2022) | 468 |
| wp:Clock_synchronization | 1372144749 | 1116046226 (14:28, 14 October 2022) | 1305 |
| wp:Comet_(programming) | 1384319543 | 1104579771 (19:21, 15 August 2022) | 2544 |
| wp:Compensating_transaction | 1318840851 | 1032179395 (23:00, 5 July 2021) | 812 |
| wp:Conflict-free_replicated_data_type | 1384255120 | 1117941241 (10:28, 24 October 2022) | 3745 |
| wp:Consensus_(computer_science) | 1371790437 | 1116217697 (12:44, 15 October 2022) | 4592 |
| wp:Consistency_model | 1372162129 | 1120580536 (19:18, 7 November 2022) | 6885 |
| wp:Consistent_hashing | 1375814388 | 1119161613 (01:29, 31 October 2022) | 1915 |
| wp:Content_delivery_network | 1384013960 | 1124163031 (17:24, 27 November 2022) | 2900 |
| wp:Content_delivery_network_interconnection | 1372414601 | 1050480400 (02:57, 18 October 2021) | 3397 |
| wp:Content-addressable_storage | 1368990452 | 1110294810 (17:30, 14 September 2022) | 3240 |
| wp:Count–min_sketch | 1368880919 | 1120830003 (01:33, 9 November 2022) | 1187 |
| wp:Data_deduplication | 1356642234 | 1063566238 (18:49, 3 January 2022) | 2743 |
| wp:Database_index | 1357770109 | 1120580139 (19:15, 7 November 2022) | 2529 |
| wp:Database_transaction_schedule (from 'Serializability') | 1373785308 | 1028188697 (12:12, 12 June 2021) | 2393 |
| wp:Dead_letter_queue | 1339507037 | 1026578228 (02:50, 3 June 2021) | 413 |
| wp:Delta_encoding | 1366131806 | 1116969537 (07:50, 19 October 2022) | 2418 |
| wp:Denormalization | 1260730598 | 1041768115 (11:03, 1 September 2021) | 709 |
| wp:Disaster_recovery | 1286358618 | none (created later)  | 85 |
| wp:Distributed_cache | 1381238137 | 1115645494 (13:39, 12 October 2022) | 353 |
| wp:Distributed_computing | 1382756877 | 1120769255 (18:45, 8 November 2022) | 6514 |
| wp:Distributed_file_system_for_cloud | 1374941482 | 1085117454 (14:22, 28 April 2022) | 7042 |
| wp:Distributed_hash_table | 1376764733 | 1121781275 (03:14, 14 November 2022) | 3011 |
| wp:Distributed_lock_manager | 1305048094 | 1089002778 (09:36, 21 May 2022) | 1526 |
| wp:Distributed_transaction | 1379749848 | 1111363225 (16:24, 20 September 2022) | 549 |
| wp:Document-oriented_database | 1374552421 | 1120853433 (04:53, 9 November 2022) | 1550 |
| wp:Domain_Name_System | 1382061679 | 1124417624 (20:39, 28 November 2022) | 8422 |
| wp:Dynamic_Adaptive_Streaming_over_HTTP | 1374898019 | 1107549766 (15:54, 30 August 2022) | 2515 |
| wp:Dynamo_(storage_system) | 1324513513 | 1031113149 (21:58, 29 June 2021) | 531 |
| wp:Edge_computing | 1383454674 | 1124276251 (04:11, 28 November 2022) | 2439 |
| wp:Elasticity_(computing) | 1347231136 | 1091097728 (05:35, 2 June 2022) | 1273 |
| wp:Erlang_(unit) | 1303140867 | 1117249230 (18:15, 20 October 2022) | 3145 |
| wp:Event-driven_architecture | 1379585711 | 1115201196 (08:21, 10 October 2022) | 2805 |
| wp:Eventual_consistency | 1374379428 | 1111258214 (02:34, 20 September 2022) | 571 |
| wp:Exponential_backoff | 1384322428 | 1106690929 (23:33, 25 August 2022) | 3141 |
| wp:Failover | 1367992837 | 1087316478 (18:33, 11 May 2022) | 645 |
| wp:Fallacies_of_distributed_computing | 1332248533 | 1123861198 (02:51, 26 November 2022) | 596 |
| wp:Fencing_(computing) | 1376703720 | 1088660733 (12:07, 19 May 2022) | 931 |
| wp:Fermi_problem | 1376729362 | 1118905767 (16:42, 29 October 2022) | 1924 |
| wp:File_synchronization | 1383109255 | 1068154811 (22:43, 26 January 2022) | 811 |
| wp:Firebase_Cloud_Messaging | 1384325061 | 1093840634 (03:53, 19 June 2022) | 2367 |
| wp:Focused_crawler | 1324240043 | 1119838584 (17:46, 3 November 2022) | 1156 |
| wp:Generic_cell_rate_algorithm | 1310767055 | 1013924784 (06:02, 24 March 2021) | 2134 |
| wp:GeoDNS | 1341102853 | 1104917471 (14:42, 17 August 2022) | 344 |
| wp:Geohash | 1383574635 | 1121497607 (16:17, 12 November 2022) | 2618 |
| wp:Google_File_System | 1373951261 | 1121867898 (15:42, 14 November 2022) | 1388 |
| wp:Gossip_protocol | 1367841355 | 1095030259 (00:28, 26 June 2022) | 1531 |
| wp:GRPC (from 'gRPC') | 1383168356 | 1124757476 (09:45, 30 November 2022) | 597 |
| wp:Hash_function | 1381471264 | 1123870368 (04:10, 26 November 2022) | 7515 |
| wp:Hash_table | 1384236591 | 1124674828 (23:12, 29 November 2022) | 6493 |
| wp:Heartbeat_(computing) | 1379094654 | 1115456769 (15:20, 11 October 2022) | 1165 |
| wp:High_availability | 1382476870 | 1117981469 (15:28, 24 October 2022) | 3450 |
| wp:HTTP | 1377007807 | 1124860497 (22:15, 30 November 2022) | 7905 |
| wp:HTTP_Live_Streaming | 1375304206 | 1124176668 (18:36, 27 November 2022) | 2678 |
| wp:HTTP/2 | 1373081544 | 1104270716 (22:04, 13 August 2022) | 3691 |
| wp:HyperLogLog | 1375654375 | 1118377112 (17:52, 26 October 2022) | 1168 |
| wp:Idempotence | 1382059785 | 1122770405 (16:33, 19 November 2022) | 2717 |
| wp:Instant_messaging | 1384064709 | 1123698825 (05:24, 25 November 2022) | 7238 |
| wp:Inverted_index | 1354610034 | 1060313151 (19:06, 14 December 2021) | 654 |
| wp:Isolation_(database_systems) | 1380380517 | 1122456713 (17:45, 17 November 2022) | 2116 |
| wp:Kademlia | 1378564784 | 1123211793 (15:36, 22 November 2022) | 3877 |
| wp:Key–value_database | 1374632217 | 1113952539 (01:29, 4 October 2022) | 613 |
| wp:Lamport_timestamp | 1381539505 | 1085873974 (22:34, 2 May 2022) | 1641 |
| wp:Latency_(engineering) | 1382111961 | 1122992065 (03:13, 21 November 2022) | 2447 |
| wp:Leader_election | 1341681953 | 1114331128 (23:53, 5 October 2022) | 3519 |
| wp:Leaky_bucket | 1351218966 | 1113649277 (15:26, 2 October 2022) | 6579 |
| wp:Linearizability | 1366605625 | 1122023445 (12:29, 15 November 2022) | 3096 |
| wp:Little's_law | 1370351232 | 1117885777 (02:26, 24 October 2022) | 1801 |
| wp:Load_balancing_(computing) | 1374334633 | 1119414906 (13:17, 1 November 2022) | 5897 |
| wp:Load_shedding | 1380633396 | 538280062 (20:04, 14 February 2013) | 470 |
| wp:Locality-sensitive_hashing | 1382893169 | 1121220653 (04:37, 11 November 2022) | 3077 |
| wp:Log-structured_merge-tree | 1374573576 | 1120239072 (23:19, 5 November 2022) | 1785 |
| wp:Logical_clock | 1359048597 | 1072010149 (14:14, 15 February 2022) | 338 |
| wp:M/M/1_queue | 1312917014 | 1083414153 (17:50, 18 April 2022) | 1439 |
| wp:Memcached | 1379813237 | 1117350566 (07:11, 21 October 2022) | 1951 |
| wp:Merkle_tree | 1383668961 | 1123544588 (08:58, 24 November 2022) | 1765 |
| wp:Message_broker | 1348235643 | 1122952171 (21:10, 20 November 2022) | 859 |
| wp:Message_queue | 1378747794 | 1118983292 (03:14, 30 October 2022) | 1964 |
| wp:Message_queuing_service | 1379708522 | 1118983261 (03:14, 30 October 2022) | 838 |
| wp:Microservices | 1378518139 | 1122416285 (13:27, 17 November 2022) | 3346 |
| wp:Multi-master_replication | 1382389043 | 1124834819 (19:21, 30 November 2022) | 1761 |
| wp:Multiversion_concurrency_control | 1381199953 | 1121379891 (00:20, 12 November 2022) | 1452 |
| wp:Network_Time_Protocol | 1382737971 | 1124509575 (02:26, 29 November 2022) | 4518 |
| wp:NoSQL | 1357603487 | 1123949416 (15:46, 26 November 2022) | 1648 |
| wp:Observability_(software) | 1369990303 | 1120332911 (12:55, 6 November 2022) | 1987 |
| wp:Operational_transformation | 1373192703 | 1084900873 (07:10, 27 April 2022) | 4886 |
| wp:Optimistic_concurrency_control | 1383954345 | 1091159570 (15:27, 2 June 2022) | 853 |
| wp:PACELC_design_principle | 1382061636 | 1122732991 (09:50, 19 November 2022) | 1128 |
| wp:Partition_(database) | 1350458844 | 1100523210 (10:31, 26 July 2022) | 1090 |
| wp:Pastebin | 1379125564 | 1087951113 (11:53, 15 May 2022) | 569 |
| wp:Paxos_(computer_science) | 1380699655 | 1120605099 (21:57, 7 November 2022) | 7016 |
| wp:Peer-to-peer | 1383611899 | 1123796320 (19:03, 25 November 2022) | 6953 |
| wp:Publish–subscribe_pattern | 1360730651 | 1119303630 (20:02, 31 October 2022) | 1525 |
| wp:Push_technology (from 'Long polling') | 1372862985 | 1121829242 (10:21, 14 November 2022) | 2513 |
| wp:Quadtree | 1376267579 | 1115215433 (10:22, 10 October 2022) | 4703 |
| wp:Queueing_theory | 1383596220 | 1122738523 (11:00, 19 November 2022) | 4243 |
| wp:Quorum_(distributed_computing) | 1382507090 | 999689185 (12:51, 11 January 2021) | 542 |
| wp:Raft_(algorithm) | 1381284725 | 1124836334 (19:31, 30 November 2022) | 2291 |
| wp:Rate_limiting | 1372842478 | 1113920411 (21:43, 3 October 2022) | 770 |
| wp:Rate-monotonic_scheduling | 1339685267 | 1105643462 (04:14, 21 August 2022) | 2614 |
| wp:Redis | 1384343938 | 1115152231 (02:09, 10 October 2022) | 2676 |
| wp:Relational_database | 1375508962 | 1116718100 (00:16, 18 October 2022) | 3199 |
| wp:Remote_procedure_call | 1383559226 | 1122759694 (14:59, 19 November 2022) | 1826 |
| wp:Rendezvous_hashing | 1384056162 | 1124809129 (16:32, 30 November 2022) | 3137 |
| wp:Replication_(computing) | 1380029215 | 1113529115 (23:18, 1 October 2022) | 2788 |
| wp:REST | 1380036165 | 1124435026 (22:31, 28 November 2022) | 1887 |
| wp:Reverse_proxy | 1383549418 | 1114110462 (21:27, 4 October 2022) | 1114 |
| wp:Robots.txt | 1383443513 | 1116592516 (10:20, 17 October 2022) | 3760 |
| wp:Round-robin_DNS | 1334865412 | 1046790621 (12:42, 27 September 2021) | 572 |
| wp:Rsync | 1370677477 | 1123625660 (19:30, 24 November 2022) | 2009 |
| wp:Scalability | 1369996964 | 1110510136 (22:20, 15 September 2022) | 1730 |
| wp:Search_engine_(computing) | 1380766394 | 1121602004 (04:31, 13 November 2022) | 2575 |
| wp:Search_engine_indexing | 1383251652 | 1122178256 (07:17, 16 November 2022) | 4268 |
| wp:Server-sent_events | 1379794477 | 1121428323 (07:02, 12 November 2022) | 475 |
| wp:Service_discovery | 1293238527 | 1119256118 (14:24, 31 October 2022) | 453 |
| wp:Service_level_indicator | 1353927134 | 1078702134 (21:58, 22 March 2022) | 151 |
| wp:Service_mesh | 1362403702 | 1123588420 (15:05, 24 November 2022) | 259 |
| wp:Service-level_agreement | 1362923384 | 1122924064 (17:18, 20 November 2022) | 1858 |
| wp:Service-level_objective | 1375493603 | 1089474535 (00:59, 24 May 2022) | 671 |
| wp:Shard_(database_architecture) | 1384144620 | 1118907386 (16:52, 29 October 2022) | 1585 |
| wp:Single_point_of_failure | 1384123072 | 1117794939 (16:36, 23 October 2022) | 1414 |
| wp:Site_reliability_engineering | 1378351869 | 1120392960 (19:34, 6 November 2022) | 1663 |
| wp:Sitemaps | 1383561230 | 1121406473 (03:42, 12 November 2022) | 2208 |
| wp:Snapshot_isolation | 1265461945 | 1099535994 (08:20, 21 July 2022) | 1335 |
| wp:Snowflake_ID | 1380690787 | 1122737836 (10:51, 19 November 2022) | 510 |
| wp:Spider_trap | 1383252843 | 1120586813 (19:55, 7 November 2022) | 414 |
| wp:Split-brain_(computing) | 1371632674 | 964293205 (17:26, 24 June 2020) | 663 |
| wp:State_machine_replication | 1375989403 | 1115458341 (15:29, 11 October 2022) | 3152 |
| wp:Stateless_protocol | 1382656567 | 1070213596 (09:07, 6 February 2022) | 565 |
| wp:Strong_consistency | 1301306883 | 1031941338 (16:30, 4 July 2021) | 83 |
| wp:Thundering_herd_problem | 1356321785 | 1123948055 (15:36, 26 November 2022) | 325 |
| wp:Time_to_live | 1339733291 | 1112268988 (13:58, 25 September 2022) | 945 |
| wp:Token_bucket | 1374879767 | 1118411592 (21:47, 26 October 2022) | 1492 |
| wp:Tracing_(software) | 1383788011 | 1094758736 (10:19, 24 June 2022) | 1405 |
| wp:Transcoding | 1370882281 | 1123925949 (12:46, 26 November 2022) | 1577 |
| wp:Transmission_Control_Protocol | 1382108671 | 1124312705 (08:43, 28 November 2022) | 13286 |
| wp:Trie | 1357162034 | 1123115896 (23:04, 21 November 2022) | 3063 |
| wp:Two_Generals'_Problem | 1376663237 | 1117902361 (04:32, 24 October 2022) | 1861 |
| wp:Two-phase_commit_protocol | 1321432957 | 1078983413 (10:48, 24 March 2022) | 1794 |
| wp:Universally_unique_identifier | 1381302778 | 1122041043 (14:48, 15 November 2022) | 6013 |
| wp:Unix_time | 1384167586 | 1123781365 (17:20, 25 November 2022) | 5668 |
| wp:URI_normalization (from 'URL normalization') | 1359957963 | 1120098126 (04:05, 5 November 2022) | 1215 |
| wp:URL_shortening | 1384315582 | 1124465619 (00:42, 29 November 2022) | 3940 |
| wp:Vector_clock | 1382371396 | 1121141841 (18:44, 10 November 2022) | 849 |
| wp:Video_on_demand | 1383616297 | 1123294958 (23:48, 22 November 2022) | 6066 |
| wp:Web_cache | 1375431709 | 1121781458 (03:16, 14 November 2022) | 503 |
| wp:Web_crawler | 1383789668 | 1124235168 (00:03, 28 November 2022) | 6892 |
| wp:Web_feed (from 'News feed') | 1383616555 | 1116868125 (19:12, 18 October 2022) | 1481 |
| wp:WebSocket | 1381019123 | 1120212787 (19:43, 5 November 2022) | 4109 |
| wp:Wide-column_store | 1379481309 | 1098683298 (00:55, 17 July 2022) | 371 |
| wp:Write-ahead_logging | 1383770856 | 1106977525 (13:02, 27 August 2022) | 467 |
| wp:XMPP | 1378343147 | 1120094990 (03:36, 5 November 2022) | 4305 |

175 articles. No article exists for 'Exactly-once delivery' or 'Sticky session' (404). 'Push notification' redirects to Push technology, which is listed (the entry records the redirect). The first 42 entries were fetched through the API before it rate-limited (their .txt is the plain extract, without `##` headings); the rest are fetched as rendered HTML text.

## 3. Link-only (fails the gate), with the reason

| item | licence found | evidence | why it's listed |
|---|---|---|---|
| karanpratapsingh/system-design | CC BY-NC-ND 4.0 | raw LICENSE: "Attribution-NonCommercial-NoDerivatives 4.0 International" | Popular full open SD course (also covers rate limiting, consistent hashing, IDs) |
| ByteByteGoHq/system-design-101 | CC BY-NC-ND 4.0 | LICENSE.md: "licensed under ... by-nc-nd/4.0" | Visual explainers |
| mixu/distsysbook ("Distributed systems for fun and profit") | all rights reserved | readme.md: "This book is available for free, but what I've written remains mine." | Short distributed-systems primer |
| Google SRE book and workbook (sre.google) | not verified (host blocked) | — | Reference for SLOs, monitoring, load balancing, overload handling |
| van Steen and Tanenbaum, *Distributed Systems* (distributed-systems.net) | not verified (host blocked) | — | Textbook, free personal copy |
| Dynamo paper (SOSP 2007), incl. the reprint at riak-docs:learn/dynamo | third-party copyright (ACM/Amazon) | riak-docs dynamo.md: "reprinted here in its entirety, images and all" | Riak's annotation boxes are CC BY; the paper text is not |
| Raft paper (USENIX ATC 2014), raft-site/raft.pdf | no licence on the paper | — | Use raft-thesis instead (same content, CC BY) |
| redis/docs (current Redis docs) | CC BY-NC-SA 4.0 | LICENSE: "licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0" | Successor of redis-doc |
| mongodb/docs | CC BY-NC-SA 3.0 | README.rst: "Creative Commons License <.../by-nc-sa/3.0/>" | Replication and sharding docs |
| Dordal, *An Introduction to Computer Networks* (LibreTexts) | CC BY-NC-ND 4.0 | LibreTexts page licence tag "CC BY-NC-ND 4.0" | Token bucket and queueing chapters (19, 20) |
| sirupsen/napkin-math | MIT (whole repo, prose included) | LICENSE: "The MIT License" | Back-of-envelope numbers; the gate admits MIT for code only. Ruling needed if the user wants it |
| aphyr/distsys-class | none found | README has no licence | Kingsbury's distributed systems class outline |
| ashishps1/awesome-system-design-resources, InterviewReady/system-design-resources, puncsky/system-design-and-architecture | GPL-3.0 | LICENSE / README "GPL v3" | Link lists and short notes |
| ulid/spec | GPL-3.0 | LICENSE | ULID spec (unique IDs) |
| twitter-archive/snowflake | no LICENSE file found at repo root (main/master) | — | Original Snowflake README |
| Apache-2.0 prose: cassandra-website (Dynamo architecture page), nats.docs, dapr/docs, istio.io, vitessio/website (sharding), linkerd, envoy docs, prometheus/docs | Apache 2.0 | LICENSE files | Rich on consistent hashing, quorums, rate limiting, back-pressure, sharding. The gate admits Apache for code only. Ruling needed |
| rabbitmq/rabbitmq-website | Apache 2.0 / MPL 2.0 | README: "dual-licensed under the Apache License 2.0 and the Mozilla Public License 2.0" | Flow control (back-pressure), acks, prefetch |
| jepsen-io/maelstrom (Gossip Glomers workloads: unique-ids, broadcast, kafka, txn) | EPL-1.0 | LICENSE | Distributed-systems exercises with a checker |
| scylladb/scylladb docs/ | unclear (no docs licence file) | docs/LICENSE.txt 404 | Ring architecture, consistency levels |
| arXiv: 1406.2294 (jump consistent hash), 1608.01350 (consistent hashing with bounded loads), 1505.00062 (multi-probe), 1812.09674 (AnchorHash), 1509.05393 (Kleppmann, critique of CAP), 1512.00168 (Viotti and Vukolić, consistency survey), 2004.05074 (Paxos vs Raft), 1608.06696 (Flexible Paxos), 1805.06358 (CRDTs), 1402.2237 | arXiv non-exclusive distribution licence | abs-page licence link "arxiv.org/licenses/nonexclusive-distrib/1.0/" | Primary papers for consistent hashing, CAP, quorums |
| arXiv 1302.0309 (Highly Available Transactions), 2008.13456 (Sequence Paxos lecture notes) | CC BY-NC-SA | abs pages | NC prose is link-only |
| arXiv 2202.06348 (Understanding Paxos) | CC BY-NC-ND 4.0 | abs page | — |
| IETF RFCs (RFC 9110 idempotent methods, RFC 2697/2698 token-bucket markers, RFC 9562 UUIDs, RFC 6585 status 429) | IETF Trust (no modification of text) | — | Normative references |
| Blogs cited by the primer (Stripe rate limiters, Instagram sharded IDs, Discord, Netflix, highscalability.com) | all rights reserved | — | Side-panel links |
| sysapproach (Peterson and Davie) | **unclear**: LICENSE is CC BY 4.0, README says the licence "does not automatically grant the right to make derivative works" | README.rst (quoted in registry) | Registered and cached anyway, as link-only until the user rules. If ruled CC BY 4.0, it covers token bucket, DNS, CDN, consistent hashing for CDNs, HTTP caching, adaptive streaming and latency maths |

### Videos (side-panel references)

YouTube search with the Creative Commons filter (`sp=EgIwAQ==`) returned the
channels below. The watch page of Kleppmann 1.1 (UEAMfLPZZhE) showed
"Creative Commons Attribution licence (reuse allowed)". Captions weren't
pulled: after a few requests YouTube answered with a `google.com/sorry` bot
check (302/429), including on `/api/timedtext`, and I did not work around
it. So all of these are link-only until captions can be fetched.

| video / series | flag | length | good for |
|---|---|---|---|
| Martin Kleppmann, "Distributed Systems" lecture series (1.1 UEAMfLPZZhE … 8.1 OqqliwwG0SM) | CC BY (verified on 1.1; others via filter) | 23 videos, 8-38 min each | Same content as kleppmann-ds; transcripts would duplicate the notes |
| MIT 6.824 Distributed Systems (cQP8WApzIQQ lecture 1; 64Zp3tzNbpE Raft; EpIgvowZr00 GFS; M_teob23ZzY primary-backup) | CC BY per filter (not verified on watch page) | ~80 min each | Raft, GFS, replication case studies |
| CMU Database Group, "Distributed Databases" lectures (IFLQBWY6dlE, pQh5fka3FC0, fyDeu_5svbg) | CC BY per filter | ~80 min each | Partitioning, replication, distributed transactions |
| ComputerNetworks UPB, "Verteilte Systeme" (German): consistent hashing 3ikJo518YqY, CAP/PACELC AWgAEjZ3aZA, message queuing wc0DUcRYcNk, Raft 3FrY5C3Slo4 | CC BY per filter | 8-35 min | German-language lectures |
| TechPrep system design videos (rate limiter dpEOhfEEoyw, KV store Uqk7IQFS-Eo, message queue Qay43Km1NwY, video streaming XAZqmLXy4kY, back-of-envelope eR5pIYfxKgY) | CC BY per filter | 8-25 min | Interview-style walkthroughs. Who wrote them, and how, is unknown: check against the no-AI rule before any use |
| EuroPython 2018, Alexys Jacob, consistent hashing in Python (erINlrgygEk) | CC BY per filter | 43 min | Consistent hashing talk |

## 4. blocked_hosts

| host | what I wanted from it |
|---|---|
| www.cl.cam.ac.uk | Kleppmann's course page and PDFs (got the LaTeX from GitHub instead) |
| martin.kleppmann.com | licence pages of blog and talks |
| book.mixu.net | "Distributed systems for fun and profit" (licence read from GitHub readme instead) |
| www.distributed-systems.net | van Steen and Tanenbaum licence/terms |
| sre.google | SRE book licence page |
| raft.github.io | Raft site (got the repo from GitHub instead) |
| bytebytego.com | licence of ByteByteGo material (repo licence read from GitHub) |
| docs.cloud.google.com (cloud.google.com redirects there) | Google Cloud architecture articles (e.g. "Rate-limiting strategies and techniques", CC BY 4.0 per the site footer) |
| export.arxiv.org | arXiv API (used the arxiv.org search pages instead) |
| open.umn.edu | Open Textbook Library search (TLS verification failed through the proxy, curl error 60) |
| jepsen.io | consistency-model pages and their licence |
| docs.aws.amazon.com, learn.microsoft.com | live docs (used the GitHub copies) |
| www.usenix.org, dl.acm.org, research.google, static.googleusercontent.com | papers' licence pages (Raft, Dynamo, Spanner, Dapper) |
| highscalability.com, brooker.co.za, jvns.ca | blogs (would be link-only anyway) |
| aosabook.org, book.systemsapproach.org, computer-networking.info | rendered sites (used the GitHub sources) |
| cassandra.apache.org, kafka.apache.org, www.postgresql.org | docs (Apache/PostgreSQL licence, link-only anyway) |
| pdos.csail.mit.edu, www.cs.cornell.edu, lamport.azurewebsites.net | MIT 6.824 notes, Cornell notes, Lamport papers |
| www.youtube.com (reachable, but bot check after a few requests) | captions of CC BY videos |
| en.wikipedia.org `/w/api.php` and `/api/rest_v1` (HTTP 429) | the API calls were rate-limited, so pages were fetched as `/wiki/` HTML plus `index.php?action=raw` instead. Not a policy block |

## 5. Notes for the judge and the user

- **Rulings that would open more material:** (1) Peterson and Davie
  (`sysapproach`): is its CC BY 4.0 LICENSE usable despite the README's
  note? (2) Apache-2.0 and MIT *prose* (Cassandra's Dynamo page, Vitess,
  NATS, napkin-math, Sonyflake/KSUID READMEs, TinyKV statements): the gate
  admits those licences for code only.
- **Pre-2023 pins cost some content.** For example, azure-arch's 2022
  throttling page has no token-bucket table, and Cloudflare's 2022 tree has
  no `load-balancing.mdx` reference architecture. HEAD commits are recorded
  in this dossier (azure-arch 629acf25, mdn 288e6441, otel 9804fb55,
  crdb 27e64c5d, etcd-site 41e5cd6a, cloudflare-docs 53ce9b50,
  syncthing-docs f0205906, k8s-site 4d973a3b, aip 2ccc61a4,
  redis-doc 10442244) if the user prefers fresher text with a per-page
  AI check.
- **MDN licence version:** CC BY-SA 2.5 s.4(b) allows adaptations under "a
  later version of this License with the same License Elements", so it
  fits the book's BY-SA 4.0. cnp3 (CC BY-SA 3.0 files) and pingcap-style
  BY-SA 3.0 work the same way.
