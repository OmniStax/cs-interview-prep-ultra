#!/usr/bin/env bash
# Fetch the registered corpus into sources/_cache/ at the versions pinned in
# sources/registry.json. Safe to rerun.
set -euo pipefail
cd "$(dirname "$0")/../sources" && mkdir -p _cache && cd _cache
clone() { # repo dir sha
  [ -d "$2" ] || git clone -q https://github.com/$1.git "$2"
  git -C "$2" fetch -q --depth 1 origin "$3" 2>/dev/null || true
  git -C "$2" checkout -q "$3"
}
clone cp-algorithms/cp-algorithms cpa d55d3f50fcccba5b7d51503baf3099d88597cb77
clone jwasham/coding-interview-university ciu 2399df2f688ba9fafe11c399cc067d7270921bb1
clone donnemartin/system-design-primer sdp ae9bbd7b02d90b9866215de185217d33f39ab733
clone patmorin/ods ods 9d22c44906dda2017b2ef0c762025bee644b58aa
clone exercism/problem-specifications exercism 7b49ec415e9169cce4aa0206d2b51ce66d98b9aa
B=https://jeffe.cs.illinois.edu/teaching/algorithms
mkdir -p jeffe jeffe-notes
for f in 00-intro 01-recursion 02-backtracking 03-dynprog 04-greedy 05-graphs 06-dfs 07-mst 08-sssp 09-apsp 10-maxflow 11-maxflowapps 12-nphard; do
  [ -f jeffe/$f.pdf ] || curl -sf -o jeffe/$f.pdf $B/book/$f.pdf; pdftotext -layout jeffe/$f.pdf jeffe/$f.txt; done
for f in A-fft B-fastexpo C-automata-dynprog D-faster-dynprog E-matroids F-pseudoflows G-mincostflow H-lp I-simplex J-approx 01-random 02-nutsbolts 03-treaps 04-chernoff 05-hashing 06-bloom 07-strings 08-mincut 09-amortize 10-scapegoat-splay 11-unionfind 12-lowerbounds 13-adversary 98-induction 99-recurrences; do
  [ -f jeffe-notes/$f.pdf ] || curl -sf -o jeffe-notes/$f.pdf $B/notes/$f.pdf; pdftotext -layout jeffe-notes/$f.pdf jeffe-notes/$f.txt; done
echo fetched
