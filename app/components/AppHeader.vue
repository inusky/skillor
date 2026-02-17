<template>
  <header class="app-header">
    <div class="app-header__inner">
      <div class="app-header__main">
        <NuxtLink class="app-header__brand" to="/">Skillor</NuxtLink>

        <nav class="app-header__nav-links" aria-label="Primary">
          <NuxtLink to="#">Overview</NuxtLink>
          <NuxtLink to="#">Resources</NuxtLink>
          <NuxtLink to="#">Contact</NuxtLink>
        </nav>
      </div>

      <div class="app-header__user-links">
        <div v-if="isSignedIn" class="app-header__user-profile">
          <span class="app-header__avatar" :title="profileLabel">
            <svg
              class="app-header__avatar-icon"
              viewBox="0 0 24 24"
              role="img"
              aria-label="User"
              fill="currentColor"
            >
              <path
                d="M12 12.15a3.75 3.75 0 1 0-3.75-3.75A3.75 3.75 0 0 0 12 12.15Z"
              />
              <path
                d="M4.5 18.9a.7.7 0 0 0 .7.7h13.6a.7.7 0 0 0 .7-.7a7.5 7.5 0 0 0-15 0Z"
              />
            </svg>
            <img
              v-if="profileImageUrl"
              class="app-header__avatar-image"
              :class="{ 'is-ready': showProfileImage }"
              :src="profileImageUrl"
              alt=""
              loading="lazy"
              @error="onAvatarError"
              @load="onAvatarLoad"
            />
          </span>
          <a href="/auth/logout">Sign Out</a>
        </div>
        <NuxtLink v-else to="/auth/sign-in">Sign In</NuxtLink>
      </div>

      <button
        class="app-header__menu-button"
        :class="{ 'is-open': isMenuOpen }"
        type="button"
        aria-label="Toggle navigation"
        aria-controls="mobile-nav-links"
        :aria-expanded="isMenuOpen"
        @click="isMenuOpen = !isMenuOpen"
      >
        <span class="app-header__menu-line" />
        <span class="app-header__menu-line" />
        <span class="app-header__menu-line" />
      </button>
    </div>

    <nav
      id="mobile-nav-links"
      class="app-header__mobile-menu"
      :class="{ 'is-open': isMenuOpen }"
      aria-label="Mobile Primary"
    >
      <NuxtLink to="/" @click="closeMenu">Home</NuxtLink>
      <NuxtLink to="/#overview" @click="closeMenu">Overview</NuxtLink>
      <NuxtLink to="/#resources" @click="closeMenu">Resources</NuxtLink>
      <NuxtLink to="/#contact" @click="closeMenu">Contact</NuxtLink>
    </nav>
  </header>
</template>

<script setup lang="ts">
const isMenuOpen = ref(false);
const authUser = useUser();
const hasImageError = ref(false);
const hasImageLoaded = ref(false);

const isSignedIn = computed(() => Boolean(authUser.value));
const profileLabel = computed(
  () => authUser.value?.name || authUser.value?.email || 'User profile',
);
const profileImageUrl = computed(() => {
  const picture = authUser.value?.picture;
  if (typeof picture !== 'string') return null;
  const trimmed = picture.trim();
  return trimmed || null;
});
const showProfileImage = computed(
  () =>
    Boolean(profileImageUrl.value) &&
    hasImageLoaded.value &&
    !hasImageError.value,
);

watch(profileImageUrl, () => {
  hasImageError.value = false;
  hasImageLoaded.value = false;
});

const onAvatarLoad = () => {
  hasImageLoaded.value = true;
  hasImageError.value = false;
};

const onAvatarError = () => {
  hasImageError.value = true;
  hasImageLoaded.value = false;
};

const closeMenu = () => {
  isMenuOpen.value = false;
};
</script>

<style scoped lang="scss">
@use '../assets/scss/config/variables' as *;

.app-header {
  position: sticky;
  top: 0;
  z-index: 40;
  opacity: 0.9;
  width: 100%;
  padding: 0 0 1.2rem;
  background: linear-gradient(
    180deg,
    rgba(250, 250, 250, 0.96) 0%,
    rgba(250, 250, 250, 0) 100%
  );
}

.app-header__inner {
  position: relative;
  isolation: isolate;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
  padding: 1.2rem 1.6rem;
  background: rgba(255, 255, 255, 0.56);
  box-shadow:
    0 28px 90px rgba(15, 23, 42, 0.1),
    0 12px 36px rgba(15, 23, 42, 0.06);
  -webkit-backdrop-filter: blur(24px) saturate(140%);
  backdrop-filter: blur(24px) saturate(140%);
}

.app-header__inner::after {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0.24),
    rgba(255, 255, 255, 0.38),
    rgba(255, 255, 255, 0.24)
  );
  opacity: 0.9;
  pointer-events: none;
}

.app-header__main {
  flex: 1 1 auto;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 2rem;
}

.app-header__brand {
  display: inline-flex;
  align-items: center;
  font-family: $titleFont;
  font-size: clamp(2rem, 2.4vw, 2.8rem);
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: $grey-900;
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.55);
}

.app-header__nav-links,
.app-header__user-links {
  display: flex;
  align-items: center;
  gap: 2.2rem;
  font-size: 1.25rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.app-header__nav-links {
  margin-left: 3rem;
}

.app-header__user-profile {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
}

.app-header__avatar {
  position: relative;
  width: 2.2rem;
  height: 2.2rem;
  min-width: 2.2rem;
  min-height: 2.2rem;
  border-radius: 50%;
  border: 1px solid rgba(30, 41, 59, 0.22);
  background: radial-gradient(
    circle at 32% 28%,
    rgba(255, 255, 255, 0.95),
    rgba(226, 232, 240, 0.82)
  );
  display: inline-flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.8),
    0 1px 3px rgba(15, 23, 42, 0.12);
}

.app-header__avatar-icon {
  width: 1.48rem;
  height: 1.48rem;
  color: #1f2937;
}

.app-header__avatar-image {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.app-header__avatar-image.is-ready {
  opacity: 1;
}

.app-header__nav-links a,
.app-header__user-links a {
  position: relative;
  color: $grey-600;
  transition: color 0.25s ease;
}

.app-header__nav-links a::after,
.app-header__user-links a::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -0.6rem;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, $blue-500, $blue-700);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.25s ease;
}

.app-header__nav-links a:hover,
.app-header__user-links a:hover {
  color: $grey-900;
}

.app-header__nav-links a:hover::after,
.app-header__user-links a:hover::after {
  transform: scaleX(1);
}

.app-header__menu-button {
  display: none;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 0.45rem;
  width: 3.6rem;
  height: 3.6rem;
  padding: 0;
  background: transparent;
  border: none;
  box-shadow: none;
  transition: transform 0.2s ease;
}

.app-header__menu-line {
  width: 2rem;
  height: 2px;
  background: $grey-900;
  border-radius: 2px;
  transition:
    transform 0.25s ease,
    opacity 0.25s ease;
}

.app-header__menu-button.is-open .app-header__menu-line:nth-child(1) {
  transform: translateY(6.5px) rotate(45deg);
}

.app-header__menu-button.is-open .app-header__menu-line:nth-child(2) {
  opacity: 0;
}

.app-header__menu-button.is-open .app-header__menu-line:nth-child(3) {
  transform: translateY(-6.5px) rotate(-45deg);
}

.app-header__menu-button:hover {
  background: transparent;
  box-shadow: none;
  transform: translateY(-1px);
}

.app-header__menu-button:focus-visible {
  outline: 2px solid $blue-700;
  outline-offset: 2px;
}

.app-header__mobile-menu {
  display: none;
}

@media (max-width: $mobileL) {
  .app-header {
    padding: 0 0 0.9rem;
  }

  .app-header__inner {
    padding: 1rem 1.2rem;
  }

  .app-header__nav-links {
    display: none;
  }

  .app-header__user-links {
    display: none;
  }

  .app-header__menu-button {
    display: inline-flex;
  }

  .app-header__mobile-menu {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    padding: 0 1.2rem;
    margin-top: 0.3rem;
    background: rgba(255, 255, 255, 0.56);
    box-shadow:
      0 28px 90px rgba(15, 23, 42, 0.1),
      0 12px 38px rgba(15, 23, 42, 0.06);
    -webkit-backdrop-filter: blur(22px) saturate(140%);
    backdrop-filter: blur(22px) saturate(140%);
    pointer-events: none;
    transition:
      max-height 0.25s ease,
      opacity 0.25s ease,
      padding 0.25s ease,
      margin-top 0.25s ease;
  }

  .app-header__mobile-menu.is-open {
    max-height: 24rem;
    opacity: 1;
    padding: 1rem 1.2rem 1.1rem;
    margin-top: 0.7rem;
    pointer-events: auto;
  }

  .app-header__mobile-menu a {
    color: $grey-700;
    font-size: 1.35rem;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
  }
}

@media (max-width: $mobileP) {
  .app-header {
    padding: 0 0 0.8rem;
  }

  .app-header__brand {
    font-size: 1.7rem;
    letter-spacing: 0.06em;
  }
}
</style>
