<template>
    <v-container
        fluid
    >
        <v-layout>
            <v-flex v-if="loading">
                <carregando
                    :text="'Carregando dados da edição'"
                />
            </v-flex>
            <v-flex
                v-else
                xs10
                offset-xs1
            >
                <v-form
                    v-model="valid"
                >
                    <v-card
                        class="pl-3"
                    >
                        <v-card-title>
                            <div class="headline">
                                Edição de área
                            </div>
                        </v-card-title>
                        <v-text-field
                            v-model="dadosLocalidade.nome"
                            label="Nome"
                            @change="atualizarCampo('nome', $event)"
                        />
                        <v-select
                            v-model="dadosLocalidade.bioma"
                            :items="getLocalidadeMetadata.bioma"
                            item-text="descricao"
                            item-value="valor"
                            label="Bioma"
                            @change="atualizarCampo('bioma', $event)"
                        />
                        <v-select
                            v-model="dadosLocalidade.clima"
                            :items="getLocalidadeMetadata.clima"
                            item-text="descricao"
                            item-value="valor"
                            label="Clima"
                            @change="atualizarCampo('clima', $event)"
                        />
                        <v-text-field
                            v-model="dadosLocalidade.cidade"
                            label="Cidade"
                            @change="atualizarCampo('cidade', $event)"
                        />
                    </v-card>
                    <v-btn
                        color="info"
                        @click="salvar()"
                    >
                        <v-icon
                            class="pr-3"
                        >save</v-icon>
                        salvar
                    </v-btn>
                    <v-btn
                        color="error"
                        @click="voltar()"
                    >
                        <v-icon
                            class="pr-3"
                        >cancel</v-icon>
                        cancelar
                    </v-btn>
                </v-form>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import _ from 'lodash';
import Carregando from '@/components/CarregandoVuetify';
import Tools from '@/mixins/tools';
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'EditarLocalidade',
    components: {
        Carregando,
    },
    mixins: [
        Tools,
    ],
    data() {
        return {
            valid: true,
            dadosEditados: {
                id: '',
                nome: '',
                bioma: '',
                clima: '',
                cidade: '',
            },
            loaded: {
                dados: false,
                metadados: false,
            },
            loading: true,
        };
    },
    computed: {
        ...mapGetters({
            dadosLocalidade: 'localidade/localidade',
            getLocalidadeMetadata: 'localidade/getLocalidadeMetadata',
        }),
        id() {
            return this.$route.params.id;
        },
    },
    watch: {
        dadosLocalidade() {
            if (this.dadosLocalidade.id !== 'undefined') {
                this.loaded.dados = true;
                this.inicializarDadosLocalidade();
            }
        },
        getLocalidadeMetadata() {
            if (this.getLocalidadeMetadata.id !== 'undefined') {
                this.loaded.metadados = true;
            }
        },
        loaded: {
            handler(value) {
                const fullyLoaded = _.keys(value).every(i => value[i]);
                if (fullyLoaded) {
                    this.loading = false;
                }
            },
            deep: true,
        },
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarLocalidade(this.$route.params.id);
            this.buscarLocalidadeMetadata();
        }
    },
    methods: {
        ...mapActions({
            buscarLocalidade: 'localidade/buscarLocalidade',
            buscarLocalidadeMetadata: 'localidade/buscarLocalidadeMetadata',
            updateLocalidade: 'localidade/updateLocalidade',
        }),
        inicializarDadosLocalidade() {
            this.dadosEditados = {
                id: this.dadosLocalidade.id,
                nome: this.dadosLocalidade.nome,
                bioma: this.dadosLocalidade.bioma,
                clima: this.dadosLocalidade.clima,
                cidade: this.dadosLocalidade.cidade,
            };
        },
        atualizarCampo(key, value) {
            if (Object.keys(this.dadosEditados).includes(key)) {
                this.dadosEditados[key] = value;
            }
        },
        salvar() {
            this.updateLocalidade(this.dadosEditados);
        },
    },
};
</script>
