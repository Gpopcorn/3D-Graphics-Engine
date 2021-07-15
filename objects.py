from colors import *

def cube():
    points = [
        [[-1], [-1], [1 ]],
        [[1 ], [-1], [1 ]],
        [[1 ], [1 ], [1 ]],
        [[-1], [1 ], [1 ]],
        [[-1], [-1], [-1]],
        [[1 ], [-1], [-1]],
        [[1 ], [1 ], [-1]],
        [[-1], [1 ], [-1]]
    ]

    edges = [
        [0, 1],
        [0, 4],
        [0, 3],
        [1, 2],
        [1, 5],
        [2, 3],
        [4, 5],
        [2, 6],
        [4, 7],
        [5, 6],
        [3, 7],
        [6, 7]
    ]

    faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [4, 0, 1, 5],
        [6, 2, 3, 7],
        [4, 0, 3, 7],
        [5, 1, 2, 6]
    ]

    return (points, edges, faces)


def pyramid():
    points = [
        [[-1], [1 ], [-1]],
        [[1 ], [1 ], [-1]],
        [[1 ], [1 ], [1 ]],
        [[-1], [1 ], [1 ]],
        [[0 ], [-1], [0 ]]
    ]

    edges = [
        [0, 1],
        [0, 3],
        [3, 2],
        [1, 2],
        [0, 4],
        [1, 4],
        [2, 4],
        [3, 4]
    ]

    faces = [
        [0, 1, 2, 3],
        [0, 1, 4],
        [0, 3, 4],
        [3, 2, 4],
        [1, 2, 4]
    ]

    return (points, edges, faces)

def sphere():
    verticies = [
        [[0.0], [0.0], [-1.0]],
        [[0.7236073017120361], [-0.5257253050804138], [-0.44721952080726624]],
        [[-0.276388019323349], [-0.8506492376327515], [-0.4472198486328125]],
        [[-0.8944262266159058], [0.0], [-0.44721561670303345]],
        [[-0.276388019323349], [0.8506492376327515], [-0.4472198486328125]],
        [[0.7236073017120361], [0.5257253050804138], [-0.44721952080726624]],
        [[0.276388019323349], [-0.8506492376327515], [0.4472198486328125]],
        [[-0.7236073017120361], [-0.5257253050804138], [0.44721952080726624]],
        [[-0.7236073017120361], [0.5257253050804138], [0.44721952080726624]],
        [[0.276388019323349], [0.8506492376327515], [0.4472198486328125]],
        [[0.8944262266159058], [0.0], [0.44721561670303345]],
        [[0.0], [0.0], [1.0]],
        [[-0.16245555877685547], [-0.49999526143074036], [-0.8506544232368469]],
        [[0.42532268166542053], [-0.30901139974594116], [-0.8506541848182678]],
        [[0.26286882162094116], [-0.8090116381645203], [-0.5257376432418823]],
        [[0.8506478667259216], [0.0], [-0.5257359147071838]],
        [[0.42532268166542053], [0.30901139974594116], [-0.8506541848182678]],
        [[-0.525729775428772], [0.0], [-0.8506516814231873]],
        [[-0.6881893873214722], [-0.49999693036079407], [-0.5257362127304077]],
        [[-0.16245555877685547], [0.49999526143074036], [-0.8506544232368469]],
        [[-0.6881893873214722], [0.49999693036079407], [-0.5257362127304077]],
        [[0.26286882162094116], [0.8090116381645203], [-0.5257376432418823]],
        [[0.9510578513145447], [-0.30901262164115906], [0.0]],
        [[0.9510578513145447], [0.30901262164115906], [0.0]],
        [[0.0], [-0.9999999403953552], [0.0]],
        [[0.5877856016159058], [-0.8090167045593262], [0.0]],
        [[-0.9510578513145447], [-0.30901262164115906], [0.0]],
        [[-0.5877856016159058], [-0.8090167045593262], [0.0]],
        [[-0.5877856016159058], [0.8090167045593262], [0.0]],
        [[-0.9510578513145447], [0.30901262164115906], [0.0]],
        [[0.5877856016159058], [0.8090167045593262], [0.0]],
        [[0.0], [0.9999999403953552], [0.0]],
        [[0.6881893873214722], [-0.49999693036079407], [0.5257362127304077]],
        [[-0.26286882162094116], [-0.8090116381645203], [0.5257376432418823]],
        [[-0.8506478667259216], [0.0], [0.5257359147071838]],
        [[-0.26286882162094116], [0.8090116381645203], [0.5257376432418823]],
        [[0.6881893873214722], [0.49999693036079407], [0.5257362127304077]],
        [[0.16245555877685547], [-0.49999526143074036], [0.8506543636322021]],
        [[0.525729775428772], [0.0], [0.8506516814231873]],
        [[-0.42532268166542053], [-0.30901139974594116], [0.8506541848182678]],
        [[-0.42532268166542053], [0.30901139974594116], [0.8506541848182678]],
        [[0.16245555877685547], [0.49999526143074036], [0.8506543636322021]]
    ]

    edges = [
        [0, 12],
        [0, 17],
        [12, 17],
        [0, 19],
        [17, 19],
        [19, 20],
        [17, 20],
        [3, 20],
        [3, 17],
        [4, 19],
        [4, 20],
        [4, 21],
        [19, 21],
        [22, 23],
        [3, 26],
        [26, 27],
        [30, 31],
        [23, 30],
        [21, 31],
        [4, 31],
        [22, 32],
        [27, 33],
        [26, 34],
        [32, 38],
        [39, 40],
        [34, 40],
        [34, 39],
        [33, 39],
        [5, 21],
        [21, 30],
        [5, 30],
        [5, 23],
        [7, 27],
        [7, 33],
        [7, 26],
        [7, 34],
        [7, 39],
        [10, 38],
        [10, 32],
        [10, 22],
        [10, 23],
        [2, 27],
        [1, 22],
        [6, 32],
        [6, 33],
        [8, 34],
        [8, 40],
        [13, 14],
        [1, 13],
        [1, 14],
        [15, 16],
        [13, 15],
        [13, 16],
        [16, 21],
        [5, 16],
        [16, 19],
        [0, 16],
        [0, 13],
        [5, 15],
        [24, 25],
        [28, 29],
        [11, 37],
        [9, 36],
        [9, 35],
        [9, 41],
        [35, 41],
        [36, 41],
        [2, 18],
        [18, 27],
        [2, 24],
        [24, 27],
        [6, 37],
        [32, 37],
        [33, 37],
        [12, 13],
        [37, 38],
        [11, 38],
        [25, 32],
        [22, 25],
        [6, 25],
        [2, 14],
        [2, 12],
        [12, 14],
        [40, 41],
        [11, 39],
        [3, 29],
        [26, 29],
        [20, 29],
        [20, 28],
        [18, 26],
        [12, 18],
        [15, 23],
        [10, 36],
        [23, 36],
        [36, 38],
        [38, 41],
        [8, 28],
        [28, 35],
        [8, 35],
        [11, 41],
        [11, 40],
        [35, 40],
        [1, 15],
        [1, 25],
        [15, 22],
        [14, 25],
        [6, 24],
        [9, 31],
        [24, 33],
        [9, 30],
        [30, 36],
        [37, 39],
        [14, 24],
        [31, 35],
        [4, 28],
        [8, 29],
        [28, 31],
        [17, 18],
        [3, 18],
        [29, 34]
    ]

    faces = [
        [0, 12, 17],
        [0, 17, 19],
        [17, 19, 20],
        [3, 17, 20],
        [4, 19, 20],
        [4, 19, 21],
        [4, 21, 31],
        [34, 39, 40],
        [5, 21, 30],
        [21, 30, 31],
        [5, 23, 30],
        [7, 27, 33],
        [7, 26, 27],
        [7, 26, 34],
        [7, 34, 39],
        [7, 33, 39],
        [10, 32, 38],
        [10, 22, 32],
        [10, 22, 23],
        [8, 34, 40],
        [1, 13, 14],
        [13, 15, 16],
        [5, 16, 21],
        [16, 19, 21],
        [0, 16, 19],
        [0, 13, 16],
        [5, 15, 16],
        [9, 35, 41],
        [9, 36, 41],
        [2, 18, 27],
        [2, 24, 27],
        [6, 32, 37],
        [0, 12, 13],
        [32, 37, 38],
        [6, 33, 37],
        [11, 37, 38],
        [6, 25, 32],
        [22, 25, 32],
        [2, 12, 14],
        [12, 13, 14],
        [3, 26, 29],
        [3, 20, 29],
        [20, 28, 29],
        [18, 26, 27],
        [2, 12, 18],
        [5, 15, 23],
        [10, 23, 36],
        [10, 36, 38],
        [36, 38, 41],
        [8, 28, 35],
        [11, 40, 41],
        [11, 39, 40],
        [11, 38, 41],
        [35, 40, 41],
        [8, 35, 40],
        [1, 13, 15],
        [1, 22, 25],
        [15, 22, 23],
        [1, 15, 22],
        [1, 14, 25],
        [6, 24, 25],
        [24, 27, 33],
        [6, 24, 33],
        [9, 30, 31],
        [9, 30, 36],
        [23, 30, 36],
        [11, 37, 39],
        [33, 37, 39],
        [2, 14, 24],
        [14, 24, 25],
        [9, 31, 35],
        [4, 20, 28],
        [8, 28, 29],
        [28, 31, 35],
        [4, 28, 31],
        [12, 17, 18],
        [3, 17, 18],
        [3, 18, 26],
        [8, 29, 34],
        [26, 29, 34]
    ]

    return (verticies, edges, faces)