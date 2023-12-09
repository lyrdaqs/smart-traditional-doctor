import { createApp } from 'vue'
import App  from './App.vue'
import * as VueRouter from 'vue-router';
import Home from './router/Home.vue';
import Fruits from './router/Fruits.vue';
import FruitDetail from './router/FruitDetail.vue';
import Medicines from './router/Medicines.vue';
import MedicineDetail from './router/MedicineDetail.vue';
import Illness from './router/Illness.vue';
import IllnesDetail from './router/IllnesDetail.vue';
import Posts from './router/Posts.vue';
import PostDetail from './router/PostDetail.vue';
import Register from './router/Register.vue';
import Login from './router/Login.vue';
import Profile from './router/Profile.vue';
import Search from './router/Search.vue';
import Ai from './router/Ai.vue';
import Admin from './router/Admin.vue';
import AdminCreate from './router/AdminCreate.vue';
import AdminUpdate from './router/AdminUpdate.vue';
import QA from './router/QA.vue';
import Contact from './router/Contact.vue';
import LoadScript from "vue-plugin-load-script";


const routes = [
    { path: '/', component: Home },
    { path: '/fruits', component: Fruits },
    { path: '/fruits/:id', component: FruitDetail },
    { path: '/medicines', component: Medicines },
    { path: '/medicines/:id', component: MedicineDetail },
    { path: '/illness', component: Illness },
    { path: '/illness/:id', component: IllnesDetail },
    { path: '/posts', component: Posts },
    { path: '/posts/:id', component: PostDetail },
    { path: '/register', component: Register },
    { path: '/login', component: Login },
    { path: '/profile', component: Profile },
    { path: '/search', component: Search },
    { path: '/ai_doctor', component: Ai },
    { path: '/admin', component: Admin },
    { path: '/admin/create', component: AdminCreate },
    { path: '/admin/update/:id', component: AdminUpdate },
    { path: '/qa', component: QA },
    { path: '/contact', component: Contact }
  ]

const router = VueRouter.createRouter({
    history: VueRouter.createWebHistory(),
    routes, 
})

const app = createApp(App);

app.use(LoadScript);
app.use(router)

app.mount("#app");