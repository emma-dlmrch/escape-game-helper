import { createStore } from "vuex"

export default createStore({
    state: {
        token:'',
        isAuthenticated: false,
        userId: '',
        gameId: '',
    },
    mutations: {
        initializeStore(state){
            if (localStorage.getItem('token') ) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
                state.userId = localStorage.getItem('userId')
                // state.gameId = localStorage.getItem('gameId')

            } else {
                state.token = ''
                state.isAuthenticated = false
            }
        },
        setToken(state,token){
            state.token = token
            state.isAuthenticated = true
            localStorage.setItem("token", token)
        },
        removeToken(state){
            state.token=''
            state.isAuthenticated = false
            localStorage.removeItem('token')
        },
        setUserId(state, userId){
            state.userId = userId
            localStorage.setItem('userId', userId)
        },
        removeUserId(state){
            state.userId = ''
            localStorage.removeItem('userId')
        },
        // setGameId(state, gameId){
        //     state.gameId = gameId
        //     localStorage.setItem('gameId', gameId)
        // }
    },
    actions : {
    },
    modules: {
        
    }
})