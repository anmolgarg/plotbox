sfood ../plotbox | sfood-graph | dot -Tps | pstopdf -i -o output/dependency_graph.pdf | xargs acroread
