<script setup>

</script>

<template>
  <transition name="route" mode="out-in">
    <router-view />
  </transition>
</template>


<style scoped>

.route-enter-active, .route-leave-active {
  transition: transform 0.5s ease, opacity 0.5s ease;
}

.route-enter-from {
  transform: translateX(100%);
  opacity: 0;
}

.route-leave-to {
  transform: translateX(-100%);
  opacity: 0;
}

</style>
