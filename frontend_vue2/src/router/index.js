import Vue from 'vue'
import VueRouter from 'vue-router'
import Properties from "@/views/Properties.vue";
import PropertyDetail from "@/views/PropertyDetail.vue";
import PropertyCreate from "@/views/PropertyCreate";
import Home from "@/views/Home.vue";

Vue.use(VueRouter)

const routes = [
  {
    path: "/propiedades/",
    name: "Properties",
    component: Properties,
  },
  {
    path: "/propiedad/:id",
    name: "PropertyDetail",
    props: true,
    component: PropertyDetail,
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/create/",
    name: "Create",
    component: PropertyCreate,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
