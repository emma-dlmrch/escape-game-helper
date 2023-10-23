import { createStore } from "vuex"

export default createStore({
    state: {
        token: '',
        isAuthenticated: false,
        userId: '',
        gameId: '',
        unlockedNodes: []
    },

    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
                state.userId = localStorage.getItem('userId')
                // state.gameId = localStorage.getItem('gameId')

            } else {
                state.token = ''
                state.isAuthenticated = false
            }
            // state.unlockedNodes:
            state.unlockedNodes = JSON.parse(localStorage.getItem('unlockedNodes') ?? "{}")
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true
            localStorage.setItem("token", token)
        },
        removeToken(state) {
            state.token = ''
            state.isAuthenticated = false
            localStorage.removeItem('token')
        },
        setUserId(state, userId) {
            state.userId = userId
            localStorage.setItem('userId', userId)
        },
        removeUserId(state) {
            state.userId = ''
            localStorage.removeItem('userId')
        },

        unlockNode(state, node) {
            var nodeExist = false;
            for (var i = 0; i< state.unlockedNodes.length; i++){                
                if (node.id == state.unlockedNodes[i].id) {
                    nodeExist = true
                    break;
                }
            }
            if (nodeExist == false) {
                state.unlockedNodes.push(node)
                localStorage.setItem('unlockedNodes', JSON.stringify(state.unlockedNodes))
            }
        },
        setNodeRead(state,node) {
            const nodeIndex = state.unlockedNodes.findIndex( n => n.id === node.id)
            node.new = false
            state.unlockedNodes[nodeIndex] = node

        },

        emptyUnlockedNodes(state){
            state.unlockedNodes = []
            localStorage.removeItem('unlockedNodes')
        },

    },

    actions: {
},
    modules: {

}
})