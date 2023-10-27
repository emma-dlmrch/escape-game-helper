import { createStore } from "vuex"
import axios from "axios";
import router from "@/router";


function parseJwt(token) {
    let base64Url = token.split('.')[1];
    let base64 = base64Url.replace('-', '+').replace('_', '/');
    return JSON.parse(window.atob(base64));
}

export default createStore({
    state: {
        token: '',
        isAuthenticated: false,
        userId: '',
        gameId: '',
        unlockedNodes: [],
        currentPlayedScenarioId: ''
    },

    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.token = JSON.parse(localStorage.getItem('token'))
                state.isAuthenticated = true
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
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true
            localStorage.setItem("token", JSON.stringify(token))
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
            localStorage.setItem('unlockedNodes', JSON.stringify(state.unlockedNodes));
        },

        setNodeResolved(state,node) {
            const nodeIndex = state.unlockedNodes.findIndex( n => n.id === node.id)
            node.resolved = true
            state.unlockedNodes[nodeIndex] = node
            localStorage.setItem('unlockedNodes', JSON.stringify(state.unlockedNodes));
        },

        setNodeInfo(state,node) {
            const nodeIndex = state.unlockedNodes.findIndex( n => n.id === node.id)
            node.info = true
            state.unlockedNodes[nodeIndex] = node
            localStorage.setItem('unlockedNodes', JSON.stringify(state.unlockedNodes));
        },

        emptyUnlockedNodes(state){
            state.unlockedNodes = []
            localStorage.removeItem('unlockedNodes')
        },

        setCurrentPlayedScenarioId(state, scenarioId) {
            state.currentPlayedScenarioId = scenarioId
            localStorage.setItem('currentPlayedScenarioId', scenarioId)
        },

    },

    actions: {
        checkTokenValidity(context){
            console.log("Validity of token is checked")
            if (this.state.token) {
                let token = JSON.parse(localStorage.getItem('token'))
                let expirationDate = parseJwt(this.state.token.access).exp
                let currentDate = Math.floor(Date.now() / 1000)

                //if token is expired logout
                if (currentDate > expirationDate) {
                    alert("Vous avez été déconnecté.e")
                    context.dispatch('logout')
                    router.push({name : 'WelcomePage'})
                // if token is expiring in less than 5 minutes, ask for a refresh 
                } else if (currentDate < expirationDate && expirationDate - currentDate < 300) {
                    axios.post('token/refresh/',{
                        refresh: token.refresh
                    })
                    .then(response => {
                        token.access = response.data.access
                        context.commit('setToken', token)
                        axios.defaults.headers.common['Authorization'] = "Bearer " + token.access
                    }, (error) => {
                        console.log(error)
                    })
                }

            }

        },

        logout(context){
            context.commit('removeToken')
            context.commit('removeUserId')
            //+redirect to main page
        }
},
    modules: {

}
})