import { createStore } from "vuex"
import axios from "axios";
import router from "@/router";

export default createStore({
    state: {
        token: '',
        isAuthenticated: false,
        userId: '',
        gameId: '',
        unlockedNodes: [],
        currentPlayedScenarioId: '',
        currentPlayedGameName:''
    },

    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.token = JSON.parse(localStorage.getItem('token'))
                state.isAuthenticated = true
                axios.defaults.headers.common['Authorization'] = "Bearer " + state.token.access
                state.userId = localStorage.getItem('userId')

            } else {
                state.token = ''
                state.isAuthenticated = false
            }

            try {
                state.unlockedNodes = JSON.parse(localStorage.getItem('unlockedNodes') ?? "[]")
            } catch (e) {
                state.unlockedNodes = "[]"
            }
            state.currentPlayedScenarioId = localStorage.getItem('currentPlayedScenarioId') ?? ''
            state.currentPlayedGameName = localStorage.getItem('currentPlayedGameName') ?? ''
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true
            axios.defaults.headers.common['Authorization'] = "Bearer " + token.access
            localStorage.setItem("token", JSON.stringify(token))
        },
        removeToken(state) {
            state.token = ''
            state.isAuthenticated = false
            delete axios.defaults.headers.common['Authorization']
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
            for (var i = 0; i < state.unlockedNodes.length; i++) {
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
        setNodeRead(state, node) {
            const nodeIndex = state.unlockedNodes.findIndex(n => n.id === node.id)
            node.new = false
            state.unlockedNodes[nodeIndex] = node
            localStorage.setItem('unlockedNodes', JSON.stringify(state.unlockedNodes));
        },

        setNodeResolved(state, node) {
            const nodeIndex = state.unlockedNodes.findIndex(n => n.id === node.id)
            node.resolved = true
            state.unlockedNodes[nodeIndex] = node
            localStorage.setItem('unlockedNodes', JSON.stringify(state.unlockedNodes));
        },

        setNodeInfo(state, node) {
            const nodeIndex = state.unlockedNodes.findIndex(n => n.id === node.id)
            node.info = true
            state.unlockedNodes[nodeIndex] = node
            localStorage.setItem('unlockedNodes', JSON.stringify(state.unlockedNodes));
        },

        emptyUnlockedNodes(state) {
            state.unlockedNodes = []
            localStorage.removeItem('unlockedNodes')
        },

        setCurrentPlayedScenarioId(state, scenarioId) {
            state.currentPlayedScenarioId = scenarioId
            localStorage.setItem('currentPlayedScenarioId', scenarioId)
        },

        setCurrentPlayedGameName(state, gameName) {
            state.currentPlayedGameName = gameName
            localStorage.setItem('currentPlayedGameName', gameName)
        },
    },

    actions: {
        logout(context) {
            context.commit('removeToken')
            context.commit('removeUserId')
            // alert("Vous avez été deconnecté.e")
            router.push({ name: 'WelcomePage' })
        },
    },
    modules: {

    }
})