import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home';
import Collections from "@/views/Collections";
import CardCreate from "@/components/CardCreate";
import CollectionsDetail from "@/views/CollectionsDetail";
import LexemeDetail from "@/views/LexemeDetail";
import Groups from "@/views/Groups";
import GroupDetail from "@/views/GroupDetail";
import PostDetail from "@/views/PostDetail";
import Database from "@/views/Database";

Vue.use(Router);

export default new Router({
    routes:[{
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/collections',
        name: 'collections',
        component: Collections
    },{
        path: '/collections/:id',
        name: 'collection',
        component: CollectionsDetail
    },{
        path: '/groups/:id',
        name: 'group',
        component: GroupDetail
    },{
        path: '/groups',
        name: 'groups',
        component: Groups
    },{
        path: '/lexeme/:id',
        name: 'lexeme',
        component: LexemeDetail
    },{
        path: '/posting/:id',
        name: 'post',
        component: PostDetail
    }
    ,{
        path: '/dataset',
        name: 'database',
        component: Database
    },
        {
            path: '/card-create',
            name: 'card-create',
            component: CardCreate
        },
    ]
})