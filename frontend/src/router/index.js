import { createRouter, createWebHistory } from "vue-router";
import Properties from "@/views/Properties.vue";

const routes = [
  {
    path: "/",
    name: "Properties",
    component: Properties,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Sales.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
