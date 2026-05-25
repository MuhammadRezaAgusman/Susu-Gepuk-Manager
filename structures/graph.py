class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, asal, tujuan, jarak):

        if asal not in self.graph:
            self.graph[asal] = {}

        self.graph[asal][tujuan] = jarak
    
    def dijkstra(self, start, end):

        # menyimpan jarak minimum
        distances = {}

        # menyimpan jalur sebelumnya
        previous = {}

        # node yang sudah dikunjungi
        visited = []

        # inisialisasi semua node
        for node in self.graph:
            distances[node] = float("inf")

        distances[start] = 0

        while True:
            current_node = None
            current_distance = float("inf")

            # cari node dengan jarak terkecil
            for node in distances:

                if node not in visited and distances[node] < current_distance:

                    current_distance = distances[node]
                    current_node = node

            # jika tidak ada node lagi
            if current_node is None:
                break

            # tandai sudah dikunjungi
            visited.append(current_node)

            # cek tetangga
            for neighbor, weight in self.graph[current_node].items():
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node


        # membangun rute
        path = []

        current = end

        while current in previous:
            path.insert(0, current)
            current = previous[current]

        path.insert(0, start)

        return distances[end], path