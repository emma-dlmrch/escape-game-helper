import {createRouter, createWebHistory} from 'vue-router'
import store from '../store/index.js'
// import PlayApp from '../components/play/PlayApp.vue'

const routes = [
    {
        path: '/manage',
        name : 'ManageGames',
        component: () => import('../components/manage/ManageApp.vue'),
        children: [
            {
                path: 'signup',
                name: 'SignUp',
                component: () => import("../components/manage/SignUp.vue")
            },
            {
                path: 'login',
                name: 'LogIn',
                component: () => import("../components/manage/LogIn.vue")
            },
            { 
                path: 'update-account',
                name: 'UpdateAccount',
                component: () => import("../components/manage/UpdateAccount.vue"),
                meta: { requiresLogin: true }
            },
            {
                path: 'games',
                name: 'GameList',
                alias: [''],
                component: () => import("../components/manage/GameList.vue"),
                meta: { requiresLogin: true }
            },
            { 
                path: 'games/:id',
                name: 'GameDetails',
                component: () => import("../components/manage/GameDetails.vue"),
                meta: { requiresLogin: true }
            },
            { 
                path: 'games/:gameId/step/:stepId',
                name: 'StepDetails',
                component: () => import("../components/manage/StepDetails.vue"),
                meta: { requiresLogin: true }
            },
            { 
                path: 'games/:gameId/step/:stepId/clue/:clueId',
                name: 'UpdateClue',
                component: () => import("../components/manage/UpdateClue.vue"),
                meta: { requiresLogin: true }
            },
            { 
                path: 'games/:gameId/scenario/:scenarioId',
                name: 'ScenarioDetails',
                component: () => import("../components/manage/ScenarioDetails.vue"),
                meta: { requiresLogin: true }
            },
            { 
                path: 'games/:gameId/scenario/:scenarioId/node/:nodeId',
                name: 'UpdateNode',
                component: () => import("../components/manage/UpdateNode.vue"),
                meta: { requiresLogin: true }
            },
            { 
                path: 'games/:gameId/scenario/:scenarioId/node/new/:parentNodeId',
                name: 'CreateNode',
                component: () => import("../components/manage/CreateNode.vue"),
                meta: { requiresLogin: true }
            },
        ]
    },
    {
        path: '/play',
        component: () => import('../components/play/PlayApp.vue'),
        children: [
            { 
                path: 'go',
                alias: [''],
                name: 'GameHomepage',
                component: () => import("../components/play/GameHomepage.vue"),
                children: [
                    
                ]
            },
            { 
                path: '',
                name: 'PlayView',
                component: () => import("../components/play/PlayView.vue"),
                children: [
                    { 
                        path: 'scenario/:scenarioId',
                        name: 'ScenarioPage',
                        component: () => import("../components/play/ScenarioPage.vue"),
                        children: [
        
                        ]
                    },
                    { 
                        path: 'step/:scenarioNodeId',
                        name: 'StepPage',
                        props: true,
                        component: () => import("../components/play/StepPage.vue"),
                    },
                ]
            },

        ]
    },

    {
        path: "/:pathMatch(.*)*",
        name: 'ErrorView',
        component: () => import('../components/common/Error.vue'),
      },
    {
        path: '/',
        name: 'WelcomePage',
        component: () => import('../components/common/WelcomePage.vue'),
    }

]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

router.beforeEach((to, from, next) => {
    // ecrire une methode qui checke la validité du token à terme
    if (to.matched.some(record => record.meta.requiresLogin) && store.state.isAuthenticated === false) {
        next({name :'LogIn'})
    } else {
        next()
    }
})