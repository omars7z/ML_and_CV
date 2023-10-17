use std::collections::{HashSet, VecDeque};
use std::io::{BufRead, Write};
use segment_tree::ops::Min;
use segment_tree::SegmentPoint;

pub struct IO<R, W: Write>(R, std::io::BufWriter<W>);

impl<R: std::io::Read, W: Write> IO<R, W> {
    pub fn new(r: R, w: W) -> IO<R, W> {
        IO(r, std::io::BufWriter::new(w))
    }
    pub fn write<S: ToString>(&mut self, s: S) {
        use std::io::Write;
        self.1.write_all(s.to_string().as_bytes()).unwrap();
    }
    pub fn read<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        let buf = self
            .0
            .by_ref()
            .bytes()
            .map(|b| b.unwrap())
            .skip_while(|&b| b == b' ' || b == b'\n' || b == b'\r' || b == b'\t')
            .take_while(|&b| b != b' ' && b != b'\n' && b != b'\r' && b != b'\t')
            .collect::<Vec<_>>();
        unsafe { std::str::from_utf8_unchecked(&buf) }
            .parse()
            .ok()
            .expect("Parse error.")
    }
    pub fn usize0(&mut self) -> usize {
        self.read::<usize>() - 1
    }
    pub fn vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.read()).collect()
    }
    pub fn chars(&mut self) -> Vec<char> {
        self.read::<String>().chars().collect()
    }
}

fn bridges_dfs(
    g: &Vec<Vec<usize>>,
    parent: usize,
    cur: usize,
    depth: usize,
    pre: &mut Vec<Option<usize>>,
    low: &mut Vec<Option<usize>>,
    edges: &mut HashSet<(usize, usize)>,
) {
    pre[cur] = Some(depth);
    low[cur] = Some(depth);
    for child in g[cur].clone() {
        if pre[child].is_none() {
            bridges_dfs(g, cur, child, depth + 1, pre, low, edges);
            low[cur] = low[cur].min(low[child]);
            if low[child] == pre[child] {
                edges.insert((cur, child));
                edges.insert((child, cur));
            }
        } else if child != parent {
            low[cur] = low[cur].min(low[child]);
        }
    }
}

fn bridges(g: &Vec<Vec<usize>>) -> HashSet<(usize, usize)> {
    let mut pre = vec![None; g.len()];
    let mut low = vec![None; g.len()];
    let mut edges = HashSet::new();
    bridges_dfs(g, 0, 0, 0, &mut pre, &mut low, &mut edges); // we already know graph is connected.
    edges
}

fn bfs_component(g: &Vec<Vec<usize>>, cur: usize, count: usize, component: &mut Vec<Option<usize>>, depth: &mut Vec<Option<usize>>) {
    let mut q = VecDeque::new();
    q.push_back((cur, 0));
    component[cur] = Some(count);
    depth[cur] = Some(0);
    while let Some((cur, d)) = q.pop_front() {
        for &child in &g[cur] {
            if component[child].is_none() {
                depth[child] = Some(d + 1);
                component[child] = Some(count);
                q.push_back((child, d + 1));
            }
        }
    }
}

fn get_components(non_bridge_edges: Vec<(usize, usize)>, n: usize) -> (Vec<bool>, Vec<usize>) {
    let mut g = vec![vec![]; n];
    let mut component: Vec<Option<usize>> = vec![None; g.len()];
    let mut depth: Vec<Option<usize>> = vec![None; g.len()];
    let mut count = 0;
    for e in &non_bridge_edges {
        g[e.0].push(e.1);
        g[e.1].push(e.0);
    }
    for node in 0..n {
        if component[node].is_none() {
            bfs_component(&g, node, count, &mut component, &mut depth);
            count += 1;
        }
    }
    let mut odd = vec![false; count];
    for e in &non_bridge_edges {
        let d1 = depth[e.0].unwrap();
        let d2 = depth[e.1].unwrap();
        if d1 % 2 == d2 % 2 {
            odd[component[e.0].unwrap()] = true;
        }
    }
    (odd, component.into_iter().map(|c| c.unwrap()).collect())
}

fn read_graph(sc: &mut IO<BufRead, std::io::StdoutLock>) -> (Vec<(usize, usize)>, Vec<Vec<usize>>) {
    let n = sc.read();
    let m = sc.read();
    let mut edges = Vec::with_capacity(m);
    for _ in 0..m {
        let u: usize = sc.read();
        let v: usize = sc.read();
        edges.push((u - 1, v - 1));
    }
    let mut g = vec![vec![]; n];
    for e in &edges {
        g[e.0].push(e.1);
        g[e.1].push(e.0);
    }
    (edges, g)
}

#[derive(Debug)]
struct Query {
    u: usize,
    v: usize,
    cu: usize,
    cv: usize,
    lca: usize,
    ans: i64,
}

fn read_queries(sc: &mut IO<BufRead, std::io::StdoutLock>) -> Vec<Query> {
    let q: usize = sc.read();
    let mut queries = Vec::with_capacity(q);
    for _ in 0..q {
        let u: usize = sc.read();
        let v: usize = sc.read();
        queries.push(Query {
            u: u - 1,
            v: v - 1,
            cu: 0,
            cv: 0,
            lca: 0,
            ans: i64::MAX,
        });
    }
    queries
}

fn dfs_g(g: &Vec<Vec<usize>>) -> Vec<(usize, usize)> {
    let mut stack = vec![0];
    let mut visited = vec![false; g.len()];
    visited[0] = true;
    let mut edges = vec![];
    while let Some(node) = stack.pop() {
        for &child in &g[node] {
            if !visited[child] {
                visited[child] = true;
                edges.push((node, child));
                stack.push(child);
            }
        }
    }
    edges
}

fn dfs_cost_below(tree: &Vec<Vec<usize>>, node: usize, cost: &mut Vec<i64>) {
    for &child in &tree[node] {
        dfs_cost_below(tree, child, cost);
        cost[node] = cost[node].min(cost[child].saturating_add(1));
    }
}

fn dfs_cost_above(tree: &Vec<Vec<usize>>, node: usize, cost: &mut Vec<i64>) {
    for &child in &tree[node] {
        cost[child] = cost[child].min(cost[node].saturating_add(1));
        dfs_cost_above(tree, child, cost);
    }
}

fn get_component_tree(sc: &mut IO<BufRead, std::io::StdoutLock>) -> (Vec<Vec<usize>>, Vec<usize>, Vec<i64>, Vec<Vec<Option<usize>>>, Vec<usize>) {
    let (edges, g) = read_graph(sc);
    let n = g.len();
    let bridge_edges = bridges(&g);
    let non_bridge_edges: Vec<(usize, usize)> = edges.iter().cloned().filter(|e| !bridge_edges.contains(e)).collect();
    let (odd, component) = get_components(non_bridge_edges, n);
    let mut tree = vec![vec![]; odd.len()];
    let mut parent: Vec<Vec<Option<usize>>> = vec![vec![None; 30]; odd.len()];
    let mut level = vec![0; odd.len()];
    for (u, v) in dfs_g(&g) {
        if component[u] != component[v] {
            level[component[v]] = level[component[u]] + 1;
            parent[component[v]][0] = Some(component[u]);
            tree[component[u]].push(component[v]);
        }
    }
    for i in 0..tree.len() {
        for k in 1..30 {
            if let Some(p) = parent[i][k - 1] {
                parent[i][k] = parent[p][k - 1];
            }
        }
    }
    let mut cost: Vec<i64> = odd.into_iter().map(|ok| if ok { 0 } else { i64::MAX }).collect();
    dfs_cost_below(&tree, 0, &mut cost);
    dfs_cost_above(&tree, 0, &mut cost);
    (tree, component, cost, parent, level)
}

fn get_lca(parent: &Vec<Vec<Option<usize>>>, mut cu: usize, mut cv: usize, level: &Vec<usize>) -> usize {
    if level[cu] < level[cv] {
        std::mem::swap(&mut cu, &mut cv);
    }
    for k in (0..30).rev() {
        if level[cu] >= level[cv] + (1 << k) && parent[cu][k].is_some() {
            cu = parent[cu][k].unwrap();
        }
    }
    if cu == cv {
        return cu;
    }
    for k in (0..30).rev() {
        if parent[cu][k] != parent[cv][k] {
            cu = parent[cu][k].unwrap_or(cu);
            cv = parent[cv][k].unwrap_or(cv);
        }
    }
    parent[cu][0].unwrap_or(cu)
}

fn dfs(tree: &Vec<Vec<usize>>, node: usize, cost: &Vec<i64>, segment_tree: &mut SegmentPoint<i64, Min>, level: &Vec<usize>, node_queries: &Vec<Vec<usize>>, queries: &mut Vec<Query>) {
    segment_tree.modify(level[node], cost[node]);
    for &i in &node_queries[node] {
        queries[i].ans = queries[i].ans.min(
            segment_tree.query(level[queries[i].lca], level[node] + 1)
        );
    }
    for &child in &tree[node] {
        dfs(&tree, child, cost, segment_tree, level, node_queries, queries);
    }
}

fn solve(sc: &mut IO<BufRead, std::io::StdoutLock>) -> i64 {
    let (tree, component, cost, parent, level) = get_component_tree(sc);
    let mut queries = read_queries(sc);
    if !cost.contains(&0) {
        return -1 * queries.len() as i64;
    }
    let mut node_queries = vec![vec![]; tree.len()];
    for q in &mut queries {
        q.cu = component[q.u];
        q.cv = component[q.v];
        q.lca = get_lca(&parent, q.cu, q.cv, &level);
    }
    for (i, q) in queries.iter().enumerate() {
        node_queries[q.cu].push(i);
        node_queries[q.cv].push(i);
    }
    let mut segment_tree = SegmentPoint::build(vec![i64::MAX; level.iter().cloned().max().unwrap() + 1], Min);
    dfs(&tree, 0, &cost, &mut segment_tree, &level, &node_queries, &mut queries);
    queries.iter().map(|q| q.ans).sum::<i64>()
}

fn main() {
    let (r, w) = (std::io::stdin(), std::io::stdout());
    let mut sc = IO::new(r.lock(), w.lock());

    let t: usize = sc.read();
    for case in 1..=t {
        let ans = solve(&mut sc);
        println!("Case #{}: {}", case, ans);
    }
}
