import {createRouter, createWebHistory} from 'vue-router'
import SignUp from '../components/manage/SignUp.vue'
import LogIn from '../components/manage/LogIn.vue'
import GameList from '../components/manage/GameList.vue'
import GameDetails from '../components/manage/GameDetails.vue'
import UpdateAccount from '../components/manage/UpdateAccount.vue'
import store from '../store/index.js'
import StepDetails from '../components/manage/StepDetails.vue'
import ScenarioDetails from '../components/manage/ScenarioDetails.vue'
import UpdateNode from '../components/manage/UpdateNode.vue'
import CreateNode from '../components/manage/CreateNode.vue'

const routes = [
    {
        path: '/signup',
        name: 'SignUp',
        component: SignUp
    },
    {
        path: '/login',
        name: 'LogIn',
        component: LogIn
    },
    { 
        path: '/update-account',
        name: 'UpdateAccount',
        component: UpdateAccount,
        meta: { requiresLogin: true }
    },
    {
        path: '/games',
        name: 'GameList',
        alias: ['/games', '/'],
        component: GameList,
        meta: { requiresLogin: true }
    },
    { 
        path: '/games/:id',
        name: 'GameDetails',
        component: GameDetails,
        meta: { requiresLogin: true }
    },
    { 
        path: '/games/:gameId/step/:stepId',
        name: 'StepDetails',
        component: StepDetails,
        meta: { requiresLogin: true }
    },
    { 
        path: '/games/:gameId/scenario/:scenarioId',
        name: 'ScenarioDetails',
        component: ScenarioDetails,
        meta: { requiresLogin: true }
    },
    { 
        path: '/games/:gameId/scenario/:scenarioId/node/:nodeId',
        name: 'UpdateNode',
        component: UpdateNode,
        meta: { requiresLogin: true }
    },
    { 
        path: '/games/:gameId/scenario/:scenarioId/node/new/:parentNodeId',
        name: 'CreateNode',
        component: CreateNode,
        meta: { requiresLogin: true }
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

router.beforeEach((to, from, next) => {
    // ecrire une methode qui checke la validité du token à terme
    if (to.matched.some(record => record.meta.requiresLogin) && store.state.isAuthenticated === false) {
        store.commit("setGlobalError", "You need to log in before you can perform this action.")
        next("/login")
    } else {
        next()
    }
})