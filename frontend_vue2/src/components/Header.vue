<template>
  <v-container fluid>
    <v-app-bar
      app
      color="#846D34"
    >
      <v-toolbar-title>
        <img class="mr-3" src="@/assets/logo.png" height="110"/>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- <v-toolbar-items class="hidden-xs-only"> -->
        <v-btn text rounded to="/" @click="$vuetify.goTo(0)" class="hidden-xs-only">Inicio</v-btn>
        <v-btn text rounded to="propiedades" class="hidden-xs-only">Alquileres</v-btn>
        <v-btn text rounded class="hidden-xs-only">Ventas</v-btn>
        <v-btn text rounded class="hidden-xs-only">Nosotros</v-btn>
        <v-btn text rounded @click="$vuetify.goTo(9999)" class="hidden-xs-only">Contacto</v-btn>
      <!-- </v-toolbar-items> -->
      <div class="hidden-sm-and-up">
        <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      </div>
    </v-app-bar>
    <v-navigation-drawer
    v-model="drawer"
    absolute
    temporary
    >
    <v-list
    nav
    dense
    >
    <v-list-item-group
    v-model="group"
    active-class="deep-purple--text text--accent-4"
    >
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-home</v-icon>
        </v-list-item-icon>
        <v-list-item-title>Inicio</v-list-item-title>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-account</v-icon>
        </v-list-item-icon>
        <v-list-item-title>Nosotros</v-list-item-title>
      </v-list-item>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-email</v-icon>
        </v-list-item-icon>
        <v-list-item-title>Contacto</v-list-item-title>
      </v-list-item>
    </v-list-item-group>
</v-list>
</v-navigation-drawer>
  </v-container>
</template>

<script>
import * as easings from 'vuetify/es5/services/goto/easing-patterns'

export default {
  name: "Header",
  data() {
    return {
      duration: 300,
      offset: 0,
      easing: 'easeInOutCubic',
      easings: Object.keys(easings),
      drawer: false,
      group: null,
    }
  },
  options () {
        return {
          duration: this.duration,
          offset: this.offset,
          easing: this.easing,
        }
  }
};
</script>
