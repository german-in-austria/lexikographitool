import Vue from 'vue';
import Router from 'vue-router';
import store from "@/store";

Vue.use(Router);

const router = new Router({
    mode: 'history',
    routes: [{
        path: '/start',
        name: 'home',

        component: () => import(/*webpackChunkName: "Home"*/ "./views/Home.vue")
    },
    {
        path: '/collections',
        name: 'collections',
        component: () => import(/*webpackChunkName: "Collections"*/ "./views/Collections.vue"),
        meta: { requiresAuth: true }
    },
    {
        path: '/search/:search',
        name: 'search',
        component: () => import(/*webpackChunkName: "Search"*/ "./views/Search.vue"),
        meta: { requiresAuth: false }
    },
    {
        path: '/',
        name: 'start',
        component: () => import(/*webpackChunkName: "Collections"*/ "./views/Start.vue"),
        meta: { requiresAuth: true }
    }, {
        path: '/collections/:id',
        name: 'collection',
        component: () => import(/*webpackChunkName: "CollectionsDetail"*/ "./views/CollectionsDetail.vue"),
        meta: { requiresAuth: true }
    }, {
        path: '/groups/:id',
        name: 'group',
        component: () => import(/*webpackChunkName: "GroupDetail"*/ "./views/GroupDetail.vue"),
        meta: { requiresAuth: true }
    }, {
        path: '/groups/join/:id/:hash',
        name: 'groupJoin',
        component: () => import(/*webpackChunkName: "GroupJoin"*/ "./views/GroupJoin.vue"),
        meta: { requiresAuth: true }
    }, {
        path: '/groups',
        name: 'groups',
        component: () => import(/*webpackChunkName: "Groups"*/ "./views/Groups.vue"),
        meta: { requiresAuth: true }
    }, {
        path: '/lexeme/:id',
        name: 'lexeme',
        component: () => import(/*webpackChunkName: "LexemeDetail"*/ "./views/LexemeDetail.vue")
    }, {
        path: '/posting/:id',
        name: 'post',
        component: () => import(/*webpackChunkName: "PostDetail"*/ "./views/PostDetail.vue")
    },
    {
        path: '/postings',
        name: 'postings',
        component: () => import(/*webpackChunkName: "Postings"*/ "./views/Postings.vue")
    }
        , {
        path: '/dataset',
        name: 'database',
        component: () => import(/*webpackChunkName: "Database"*/ "./views/Database.vue")
    },
    {
        path: '/card-create',
        name: 'card-create',
        component: () => import(/*webpackChunkName: "CardCreate"*/ "./components/CardCreate.vue"),
        meta: { requiresAuth: true }
    },
    {
        path: '/lexemes',
        name: 'lexemes',
        component: () => import(/*webpackChunkName: "Lexemes"*/ "./views/Lexemes.vue"),
        meta: { requiresAuth: false }
    },

    {
        path: '/account',
        name: 'account',
        component: () => import(/*webpackChunkName: "Account"*/ "./views/Settings.vue"),
        meta: { requiresAuth: true }
    },
    {
        path: '/login',
        name: 'login',
        component: () => import(/*webpackChunkName: "Login"*/ "./views/Login.vue"),
    },
    ]
})
router.beforeEach((to, from, next) => {

    if (to.matched.some(record => record.meta.requiresAuth)) {
        const isAuthenticated = store.getters['auth/authenticated'];

        if (!isAuthenticated) {
            next({
                name: "login",
                query: {
                    nextUrl: to.fullPath,
                }
            });
        } else {
            next();
        }
    } else {
        next()
    }
})

export default router