import { createRouter, createWebHistory } from "vue-router";
import Properties from "@/views/Properties.vue";
import PropertyDetail from "@/views/PropertyDetail.vue";

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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
