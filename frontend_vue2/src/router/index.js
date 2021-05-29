import Vue from 'vue'
import VueRouter from 'vue-router'
import Properties from "@/views/Properties.vue";
import PropertyDetail from "@/views/PropertyDetail.vue";

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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
