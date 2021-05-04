import Vue from 'vue';
import VueRouter from 'vue-router';
import store from "@/store";
import VueMeta from 'vue-meta'
import PostDetail from "@/views/PostDetail";
import LexemeEdit from "@/views/LexemeEdit";
import Postings from "@/views/Postings";
import CardCreate from "@/components/CardCreate";
import Start from "@/views/Start";
import Collections from "@/views/Collections";
import Dashboard from "@/views/Dashboard";
import Search from "@/views/Search";
import CollectionsDetail from "@/views/CollectionsDetail";
import GroupDetail from "@/views/GroupDetail";
import GroupJoin from "@/views/GroupJoin";
import Groups from "@/views/Groups";
import LexemeDetail from "@/views/LexemeDetail";
import Settings from "@/views/Settings";
import Lexemes from "@/views/Lexemes";
import Login from "@/views/Login";
import Reports from "@/views/Reports";
import Imprint from "@/views/Imprint";
import DataProtection from "@/views/DataProtection";
import Highscore from "@/views/Highscore";

Vue.use(VueRouter);
Vue.use(VueMeta,{
    keyName: 'head'
})
const router = new VueRouter({
    mode: 'history',
    scrollBehavior (to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        } else {
            return { x: 0, y: 0 }
        }
    },

    routes: [{
        path: '/start',
        name: 'start',

        // component: () => import(/*webpackChunkName: "Start"*/ "./views/Home.vue")
        component: Start
    },
        {
            path: '/collections',
            name: 'collections',
            component: Collections,
            meta: {requiresAuth: true}
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: Dashboard,
            meta: {requiresAuth: true}
        },
        {
            path: '/search/:search',
            name: 'search',
            component: Search,
            meta: {requiresAuth: false}
        },
        {
            path: '/',
            name: 'Home',
            // component: () => import(/*webpackChunkName: "Collections"*/ "./views/Start.vue"),
            component: Lexemes,
            meta: {requiresAuth: false}
        }, {
            path: '/collections/:id',
            name: 'collection',
            component: CollectionsDetail,
            meta: {requiresAuth: true}
        }, {
            path: '/groups/:id',
            name: 'group',
            component: GroupDetail,
            meta: {requiresAuth: true}
        }, {
            path: '/groups/join/:id/:hash',
            name: 'groupJoin',
            component: GroupJoin,
            meta: {requiresAuth: true}
        }, {
            path: '/groups',
            name: 'groups',
            component: Groups,
            meta: {requiresAuth: true}
        }, {
            path: '/lexeme/:id',
            name: 'lexeme',
            component: LexemeDetail
        }, {
            path: '/posting/:id',
            name: 'post',
            component: PostDetail
        },
        {
            path: '/lexeme_Edit/:id',
            name: 'lexemeEdit',
            component: LexemeEdit,
            meta: {requiresAuth: true}

        },
        {
            path: '/postings',
            name: 'postings',
            component: Postings
        }
        ,
        {
            path: '/card-create',
            name: 'card-create',
            component: CardCreate,
            meta: {requiresAuth: true}
        },
        {
            path: '/lexemes',
            name: 'lexemes',
            component: Lexemes,
            meta: {requiresAuth: false}
        },

        {
            path: '/account',
            name: 'account',
            component: Settings,
            meta: {requiresAuth: true}
        },
        {
            path: '/login',
            name: 'login',
            component: Login,
        }, {
            path: '/reports',
            name: 'reports',
            component: Reports,
            meta: {requiresSuperUser: true}

        }, {
            path: '/highscore',
            name: 'highscore',
            component: Highscore,

        },
        {
            path: '/imprint',
            name: 'imprint',
            component: Imprint,

        },{
            path: '/dataprotection',
            name: 'dataprotection',
            component: DataProtection,

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
            }
        }

    if (to.matched.some(record => record.meta.requiresSuperUser)) {
        const isSuperUser = store.getters['auth/isSuperUser'];

        if (!isSuperUser) {
            next({
                name: "login",
                query: {
                    nextUrl: to.fullPath,
                }
            });
        }
    }
        next();
    }
)

export default router