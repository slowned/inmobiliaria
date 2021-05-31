<template>
  <v-container fluid>
    <v-app-bar
      app

    >
      <v-toolbar-title>
        <img class="mr-3" src="@/assets/logo.png" height="110"/>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- <v-toolbar-items class="hidden-xs-only"> -->
        <v-btn text rounded to="/">Inicio</v-btn>
        <v-btn text rounded to="propiedades">Alquileres</v-btn>
        <v-btn text rounded >Ventas</v-btn>
        <v-btn text rounded >Nosotros</v-btn>
        <v-btn text rounded @click="$vuetify.goTo(9999)">Contacto</v-btn>
      <!-- </v-toolbar-items> -->
      <div class="hidden-sm-and-up">
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-app-bar-nav-icon v-on="on"></v-app-bar-nav-icon>
          </template>
          <v-list class="responsiveMenu">
            <v-list-item>
              <v-list-item-title><v-btn text :to="{ name: 'Home' }">Inicio</v-btn></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><v-btn text :to="{ name: 'Properties' }">Alquileres</v-btn></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><v-btn text  :to="{ }">Ventas</v-btn></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><v-btn text :to="{ }">Nosotros</v-btn></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><v-btn text @click="$vuetify.goTo(9999)" :to="{ }">Contacto</v-btn></v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
    </v-app-bar>
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
