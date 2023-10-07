import { createStore } from "vuex"
import axios from "axios"

export default createStore({
    state: {
        token:'',
        isAuthenticated: false,
        userId: null, //this is just for displaying purposes. If absence of need is confirmed, remove library jwt decode from the project
        gameId: null
    },
    mutations: {
        initializeStore(state){
            if (localStorage.getItem('token') ) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
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
        },
        setGameId(state, gameId){
            state.gameId = gameId
        }
    },
    actions : {
        getGameDetails(state, gameId){
            axios.get("/game/" + gameId)
            .then(response => {
                console.log(response);
            })
            .catch(error => {
                console.log(error);

            })
        },
    },
    modules: {
        
    }
})